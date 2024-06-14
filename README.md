### Script Liquidswap V1 
Current python script is designed to allow you create aptos-cli commands to add liquidity to huge amount of bins.

To create liquidity adding commands you should edit few variables in script:
1. active_bin_id - active bin id of selected pool.
2. liquidswap_cl_addr - address of liquidswap in selected network.
3. coin_x, coin_y - paths to coin resources.
4. bin_steps - bin step of selected pool.
5. bin_slippage - price changes by how many bins will suit you.
6. total_x - amount of coins X to add as liquidity.
7. total_y - amount of coins Y to add as liquidity.
8. start_left, end_left - range of bins for Y liquidity.
9. start_right, end_right - range of bins for X liquidity.

### Run script:
```bash
python3 script.py
```