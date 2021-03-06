#!/usr/bin/env python3

#fsTimer - free, open source software for race timing.
#Copyright 2012-17 Ben Letham

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

#The author/copyright holder can be contacted at bletham@gmail.com

'''Printer class for html files for multi lap races'''

from fstimer.printer.printer import Printer

class LapPrinter(Printer):
    '''Printer class for multi lap races'''

    def common_entry(self, row):
        '''Returns the common part of the printout of the entry
           of a given runner for scratch or by category results
           @type bibid: string'''
        # first line, as before
        row_print = list(row)
        if 'Lap Times' in self.fields:
            idx_lap = self.fields.index('Lap Times')
            lap_times = row[idx_lap]  # Take from str back to list
            row_print[idx_lap] = lap_times[0]
        entry = self.row_delim.join(row_print)
        if 'Lap Times' in self.fields:
            for i in range(1, len(lap_times)):
                # delim for Place
                entry += self.row_end + self.row_start + self.row_delim  
                row_print = ['' for j in range(len(row))]
                row_print[idx_lap] = str(lap_times[i])
                entry += self.row_delim.join(row_print)
        return entry
