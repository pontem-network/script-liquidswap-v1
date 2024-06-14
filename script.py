active_bin_id = '8394096'
liquidswap_cl_addr = '0xc9ccc585c8e1455a5c0ae4e068897a47e7c16cf16f14e0655e3573c2bbc76d48'
coin_x = '0x43417434fd869edee76cca2a4d2301e528a1551b1d719b75c350c3c97d15b8b9::coins::USDT'
coin_y = '0x1::aptos_coin::AptosCoin'
bin_steps = 'X5'
bin_slippage = '0'  # price changes by how many bins will suit you. Set to 0 if you want to add liquidity only at the current price

total_x = '30000'
total_y = '30000'

start_left = 8394093
end_left = 8394096

start_right = 8394096
end_right = 8394099


def liq(start, end, is_left):
    length = (end + 1) - start
    array = [start + i for i in range(length)]

    bins_string = '\'u32:[' + ', '.join(f'"{value}"' for value in array) + ']\''

    if is_left:
        liq_x = [0] * length
        liq_y = [int(total_y) // length] * length
    else:
        liq_x = [int(total_x) // length] * length
        liq_y = [0] * length

    liq_x_string = '\'u64:[' + ', '.join(f'"{value}"' for value in liq_x) + ']\''
    liq_y_string = '\'u64:[' + ', '.join(f'"{value}"' for value in liq_y) + ']\''

    if is_left:
        total_x_to_use = '0'
        total_y_to_use = total_y
    else:
        total_x_to_use = total_x
        total_y_to_use = '0'

    command = 'aptos move run --function-id ' + liquidswap_cl_addr + '::entry::add_liquidity --type-args ' + coin_x + ' ' + coin_y + ' ' + liquidswap_cl_addr + '::bin_steps::' + bin_steps + ' --args u64:' + total_x_to_use + ' u64:' + total_y_to_use + ' ' + bins_string + ' u32:' + active_bin_id + ' u32:' + bin_slippage + ' ' + liq_x_string + ' ' + liq_y_string + ' u64:0 u64:0 --profile Test'

    print(command)


liq(start_left, end_left, True)
liq(start_right, end_right, False)
