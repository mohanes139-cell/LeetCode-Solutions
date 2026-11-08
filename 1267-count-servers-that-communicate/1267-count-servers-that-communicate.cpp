#include <vector>

class Solution {
public:
    int countServers(std::vector<std::vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        std::vector<int> row_count(m, 0);
        std::vector<int> col_count(n, 0);
        
        // Pass 1: Count total servers in each row and column
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 1) {
                    row_count[r]++;
                    col_count[c]++;
                }
            }
        }
        
        int connected_servers = 0;
        
        // Pass 2: Count servers sharing a row or column with others
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 1) {
                    if (row_count[r] > 1 || col_count[c] > 1) {
                        connected_servers++;
                    }
                }
            }
        }
        
        return connected_servers;
    }
};