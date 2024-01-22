import pathlib
from typing import Union
import json
from pathlib import Path

def parse_positions_file(filename: Union[str, pathlib.Path], 
                mm_version: float = 2.0, positions_type: str = 'grid'):
    """
    Takes a positions file in micromanager and returns and dictionary of
    positions and microscope properties

    Args:
        filename (str | pathlib.path): 
        mm_version: 
        positions_type (str): 'grid' or 'corners'

    Returns:
        microscope_props (dict):
        positions (dict):
    """
    filename = filename if isinstance(filename, pathlib.Path) else Path(filename)
    microscope_props = {}
    positions = []

    if not filename.exists():
        raise FileNotFoundError(f'Filename {filename} not found')
    
    if filename.suffix != '.pos':
        raise ValueError(f'Position filename {filename} does not have .pos extenstion')

    with open(filename, 'r') as fh:
        data = json.load(fh)
    
    microscope_props['mm_major_version'] = data['major_version']
    microscope_props['mm_minor_version'] = data['minor_version']

    positions_dicts = data['map']['StagePositions']['array']

    if len(positions_dicts) == 0:
        raise ValueError(f'No positions found in positions file {filename.name}')
        return microscope_props, positions
    
    defaultXYStage = positions_dicts[0]['DefaultXYStage']['scalar']
    defaultZStage = positions_dicts[0]['DefaultZStage']['scalar']

    microscope_props['XYStage'] = defaultXYStage
    microscope_props['ZStage'] = defaultZStage

    # Sometimes index of devices can be a bit off so you have to look for the
    # correct order
    XYDeviceIndex = None
    ZDeviceIndex = None
    first_position = positions_dicts[0]['DevicePositions']['array']
    for i, item in enumerate(first_position, 0):
        if item['Device']['scalar'] == defaultXYStage:
            XYDeviceIndex = i
        elif item['Device']['scalar'] == defaultZStage:
            ZDeviceIndex = i
    
    for position_item in positions_dicts:
        X = position_item['DevicePositions']['array'][XYDeviceIndex]['Position_um']['array'][0] # XYStage device is on list item 1
        Y = position_item['DevicePositions']['array'][XYDeviceIndex]['Position_um']['array'][1] # XYStage device is on list item 1
        Z = position_item['DevicePositions']['array'][ZDeviceIndex]['Position_um']['array'][0] # PFSoffset device is on list item 0
        grid_row = position_item['GridRow']['scalar']
        grid_col = position_item['GridCol']['scalar']
        label = position_item['Label']['scalar']
        positions.append({'x': X, 'y': Y, 'z': Z, 'grid_row': grid_row,
                        'grid_col': grid_col, 'label': label})
    
    # find the ranges of x and y to make it easier to write
    # movement bounds
    x_values = [item['x'] for item in positions]
    y_values = [item['y'] for item in positions]
    z_values = [item['z'] for item in positions]
    
    microscope_props['x_range'] = (min(x_values), max(x_values))
    microscope_props['y_range'] = (min(y_values), max(y_values))
    microscope_props['z_range'] = (min(z_values), max(z_values))

    if positions_type == 'grid':
        # sort them by positon number if you want to reload positions later on
        # to generate events
        positions = sorted(positions, key= lambda x: int(x['label'][3:]))
    
    # if positoins_type == 'corners' you just want positions, 
    # we don't care about the order as labels will 'PosTL1', 'PosTR1', ..

    return microscope_props, positions
    
        



    
