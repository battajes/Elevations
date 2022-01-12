'''CSC108: Assignment 2
Author: Jessica Batta
'''

from typing import List


THREE_BY_THREE = [[1, 2, 1],
                  [4, 6, 5],
                  [7, 8, 9]]

FOUR_BY_FOUR = [[1, 2, 6, 5],
                [4, 5, 3, 2],
                [7, 9, 8, 1],
                [1, 2, 1, 4]]

UNIQUE_3X3 = [[1, 2, 3],
              [9, 8, 7],
              [4, 5, 6]]

UNIQUE_4X4 = [[10, 2, 3, 30],
              [9, 8, 7, 11],
              [4, 5, 6, 12],
              [13, 14, 15, 16]]


def compare_elevations_within_row(elevation_map: List[List[int]], map_row: int,
                                  level: int) -> List[int]:
    '''Return a new list containing three counts: the number of elevations 
    from row number map_row of elevation_map that are less than, equal to, 
    and greater than elevation level.

    Precondition: elevation_map is a valid elevation map.
                  0 <= map_row < len(elevation_map).

    >>> compare_elevations_within_row(THREE_BY_THREE, 1, 5)
    [1, 1, 1]
    >>> compare_elevations_within_row(FOUR_BY_FOUR, 1, 2)
    [0, 1, 3]
    '''
    elevation = [0, 0, 0]
    for i in range(len(elevation_map[map_row])):
        if elevation_map[map_row][i] > level:
            elevation[2] += 1
        elif elevation_map[map_row][i] < level:
            elevation[0] += 1
        else:
            elevation[1] += 1
    return elevation

def update_elevation(elevation_map: List[List[int]], start: List[int],
                     stop: List[int], delta: int) -> None:
    '''Modify elevation_map so that the elevation of each cell 
    between cells start and stop, inclusive, changes by amount  delta.

    Precondition: elevation_map is a valid elevation map.
                  start and stop are valid cells in elevation_map.
                  start and stop are in the same row or column or both.
                  If start and stop are in the same row,
                      start's column <=  stop's column.
                  If start and stop are in the same column,
                      start's row <=  stop's row.
                  elevation_map[i, j] + delta >= 1
                      for each cell [i, j] that will change.

    >>> THREE_BY_THREE_COPY = [[1, 2, 1],
    ...                        [4, 6, 5],
    ...                        [7, 8, 9]]
    >>> update_elevation(THREE_BY_THREE_COPY, [1, 0], [1, 1], -2)
    >>> THREE_BY_THREE_COPY
    [[1, 2, 1], [2, 4, 5], [7, 8, 9]]
    >>> FOUR_BY_FOUR_COPY = [[1, 2, 6, 5],
    ...                      [4, 5, 3, 2],
    ...                      [7, 9, 8, 1],
    ...                      [1, 2, 1, 4]]
    >>> update_elevation(FOUR_BY_FOUR_COPY, [1, 2], [3, 2], 1)
    >>> FOUR_BY_FOUR_COPY
    [[1, 2, 6, 5], [4, 5, 4, 2], [7, 9, 9, 1], [1, 2, 2, 4]]

    '''

    if start[0] == stop[0]:
        for i in range(start[1], stop[1] + 1):
            elevation_map[start[0]][i] += delta
    else:
        for i in range(start[0], stop[0] + 1):
            elevation_map[i][stop[1]] += delta


def get_average_elevation(elevation_map: List[List[int]]) -> float:
    '''Return the average elevation across all cells in elevation_map.

    Precondition: elevation_map is a valid elevation map.

    >>> get_average_elevation(UNIQUE_3X3)
    5.0
    >>> get_average_elevation(FOUR_BY_FOUR)
    3.8125
    '''

    average = []
    
    for lst in elevation_map:
        count = 0
        for cell in lst:
            count = count + cell
        average.append(count / len(lst))
    return sum(average) / len(average)   


def find_peak(elevation_map: List[List[int]]) -> List[int]:
    '''Return the cell that is the highest point in the elevation_map.

    Precondition: elevation_map is a valid elevation map.
                  Every elevation value in elevation_map is unique.

    >>> find_peak(UNIQUE_3X3)
    [1, 0]
    >>> find_peak(UNIQUE_4X4)
    [0, 3]
    '''
    
    max_elev = 0
    peak = [0, 0]
    for row in range(len(elevation_map)):
        for column in range(len(elevation_map)):
            if elevation_map[row][column] > max_elev:
                max_elev = elevation_map[row][column]
                peak[0] = row
                peak[1] = column
    return peak


def is_sink(elevation_map: List[List[int]], cell: List[int]) -> bool:
    '''Return True if and only if cell exists in the elevation_map
    and cell is a sink.

    Precondition: elevation_map is a valid elevation map.
                  cell is a 2-element list.

    >>> is_sink(THREE_BY_THREE, [0, 5])
    False
    >>> is_sink(THREE_BY_THREE, [0, 2])
    True
    >>> is_sink(THREE_BY_THREE, [1, 1])
    False
    >>> is_sink(FOUR_BY_FOUR, [2, 3])
    True
    >>> is_sink(FOUR_BY_FOUR, [3, 2])
    True
    >>> is_sink(FOUR_BY_FOUR, [1, 3])
    False
    '''

   
    if (cell[0] >= len(elevation_map) or cell[1] >= len(elevation_map[0])):
        return False
    

    max1 = max(0, cell[0]-1)
    min1 = min(len(elevation_map), cell[0] + 2)

    max2 = max(0, cell[1]-1)
    min2 = min(len(elevation_map[0]), cell[1] + 2)

   
    for i in range(max1, min1):
        for j in range(max2, min2):
            if elevation_map[cell[0]][cell[1]] > elevation_map[i][j]:
                return False
    return True
        

def find_local_sink(elevation_map: List[List[int]],
                    cell: List[int]) -> List[int]:
    '''Return the local sink of cell cell in elevation_map.

    Precondition: elevation_map is a valid elevation map.
                  elevation_map contains no duplicate elevation values.
                  cell is a valid cell in elevation_map.

    >>> find_local_sink(UNIQUE_3X3, [1, 1])
    [0, 0]
    >>> find_local_sink(UNIQUE_3X3, [2, 0])
    [2, 0]
    >>> find_local_sink(UNIQUE_4X4, [1, 3])
    [0, 2]
    >>> find_local_sink(UNIQUE_4X4, [2, 2])
    [2, 1]
    '''
    
    max1 = max(0, cell[0]-1)
    min1 = min(len(elevation_map), cell[0] + 2)

    max2 = max(0, cell[1]-1)
    min2 = min(len(elevation_map[0]), cell[1] + 2)
    local_min = float('inf')
    lst = []

    for i in range(max1, min1):
        for j in range(max2, min2):
            if elevation_map[i][j] < local_min:
                local_min = elevation_map[i][j]
                lst = [i, j]
    return lst
        

def can_hike_to(elevation_map: List[List[int]], start: List[int],
                dest: List[int], supplies: int) -> bool:
    '''Return True if and only if a hiker can move from start to dest in
    elevation_map without running out of supplies.

    Precondition: elevation_map is a valid elevation map.
                  start and dest are valid cells in elevation_map.
                  dest is North-West of start.
                  supplies >= 0

    >>> map = [[1, 6, 5, 6],
    ...        [2, 5, 6, 8],
    ...        [7, 2, 8, 1],
    ...        [4, 4, 7, 3]]
    >>> can_hike_to(map, [3, 3], [2, 2], 10)
    True
    >>> can_hike_to(map, [3, 3], [2, 2], 8)
    False
    >>> can_hike_to(map, [3, 3], [3, 0], 7)
    True
    >>> can_hike_to(map, [3, 3], [3, 0], 6)
    False
    >>> can_hike_to(map, [3, 3], [0, 0], 18)
    True
    >>> can_hike_to(map, [3, 3], [0, 0], 17)
    False
    '''
    
    
    cell = [start[0], start[1]]
    x = elevation_map
    a = abs(x[cell[0]][cell[1]] - x[cell[0]][cell[1] - 1])
    b = abs(x[cell[0]][cell[1]] - x[cell[0] - 1][cell[1]])
    
    while not cell == dest:
        if cell[0] == dest[0]:
            supplies -= abs(x[cell[0]][cell[1]] - x[cell[0]][cell[1] - 1])
            if supplies >= 0:
                cell[1] = cell[1] - 1
            else:
                return False
            
        elif cell[1] == dest[1]:
            supplies -= abs(x[cell[0]][cell[1]] - x[cell[0] - 1][cell[1]])
            if supplies >= 0:
                cell[0] = cell[0] - 1
            else:
                return False
            
        elif a < b:
            supplies -= abs(x[cell[0]][cell[1]] - x[cell[0]][cell[1] - 1])
            if supplies >= 0:
                cell[1] = cell[1] - 1
            else:
                return False
        else:
            supplies -= abs(x[cell[0]][cell[1]] - x[cell[0] - 1][cell[1]])
            if supplies >= 0:
                cell[0] = cell[0] - 1
            else:
                return False
    return True
   

def get_lower_resolution(elevation_map: List[List[int]]) -> List[List[int]]:
    '''Return a new elevation map, which is constructed from the values
    of elevation_map by decreasing the number of points within it.

    Precondition: elevation_map is a valid elevation map.

    >>> get_lower_resolution(
    ...     [[1, 6, 5, 6],
    ...      [2, 5, 6, 8],
    ...      [7, 2, 8, 1],
    ...      [4, 4, 7, 3]])
    [[3, 6], [4, 4]]
    >>> get_lower_resolution(
    ...     [[7, 9, 1],
    ...      [4, 2, 1],
    ...      [3, 2, 3]])
    [[5, 1], [2, 3]]
    '''
    nmap = []
    total = 0
    nrow = 0
    length = len(elevation_map)
    
    for row in range(0, length, 2):
        nmap.append([])
        for column in range(0, length, 2):
            total = elevation_map[row][column]
            point = 1

            if row + 1 < length:
                total += elevation_map[row + 1][column]
                point += 1

            if column + 1 < length:
                total += elevation_map[row][column + 1]
                point += 1

            if (row + 1) < length and (column + 1) < length:
                total += elevation_map[row + 1][column + 1]
                point += 1

            nmap[nrow].append(total // point)
        nrow += 1
    return nmap


if __name__ == '__main__':
    import doctest
    doctest.testmod()

                    
   
