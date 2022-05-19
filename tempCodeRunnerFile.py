                                try:
                                    self.tiles[curr_tile_x][curr_tile_y].neighbours.append(self.tiles[curr_tile_x + x_offset][curr_tile_y + y_offset])
                                    if self.tiles[curr_tile_x + x_offset][curr_tile_y + y_offset].is_bomb:
                                        self.tiles[curr_tile_x][curr_tile_y].nearby_bombs += 1
                                except:
                                    print("error")
                                    continue