def arrange_calculation(self):
        coords_data = self.coords_calculation()
        if not coords_data: return
        self.Process_clear()

        try:
            # 1. 基礎參數提取
            wire_diam = self.in_pa_001.value()
            wire_rad = wire_diam / 2
            ab_l, bc_l, cd_l = coords_data["AB"], coords_data["BC"], coords_data["CD"]
            ax, ay = coords_data["A"]
            
            # 2. 排線幾何常數
            # 第 2 層後的高度補正 (√3/2 * d)
            layer_pitch = (math.sqrt(3) / 2) * wire_diam 
            slope = (ay - coords_data["D"][1]) / (ax - coords_data["D"][0])
            
            # 3. 建立統一字典
            self.winding_results = {}
            total_turns = 0

            # --- 第一部分：方形區排列 (Square Layers) ---
            for i in range(1, square_layers_AB + 1):
                layer_key = f"L{i}"
                map_x = (2 * wire_rad) if i % 2 == 0 else wire_rad
                map_y = wire_rad + (i - 1) * layer_pitch
                map_turns = int((bc_l - (map_x - wire_rad)) / wire_diam)
                
                self.winding_results[layer_key] = (map_x, map_y, map_turns)
                total_turns += map_turns
                self.Process.append(f"{layer_key} (方): X={map_x:.3f}, 圈數={map_turns}")

            # --- 第二部分：三角形斜邊區 (Triangle Layers) ---
            # 直線方程式 A, B, C
            eq_A, eq_B, eq_C = -slope, 1, (slope * ax - ay)

            for j in range(1, triangle_layers_AB + 1):
                layer_num = square_layers_AB + j
                layer_key = f"L{layer_num}"
                
                map_x = (2 * wire_rad) if layer_num % 2 == 0 else wire_rad
                map_y = wire_rad + (layer_num - 1) * layer_pitch
                
                # 利用 while 迴圈精確計算每一層能塞幾根，直到撞到 AD 斜邊
                current_turns = 0
                while True:
                    test_x = map_x + (current_turns * wire_diam)
                    # 點到直線距離公式
                    dist = abs(eq_A * test_x + eq_B * map_y + eq_C) / math.sqrt(eq_A**2 + eq_B**2)
                    
                    # 判斷：不能超過右邊界 C 點，且不能撞到 AD 斜邊
                    if (test_x + wire_rad) > bc_l or dist < wire_rad:
                        break
                    current_turns += 1
                
                if current_turns <= 0: break
                
                self.winding_results[layer_key] = (map_x, map_y, current_turns)
                total_turns += current_turns
                self.Process.append(f"{layer_key} (斜): X={map_x:.3f}, 圈數={current_turns}")

            # 4. 更新 UI 顯示
            self.Process.append(f"\n[計算完成] 總累計圈數: {total_turns} 圈")
            self.Sectional_area.setValue(math.pi * (wire_rad**2)) # 修正拼字

        except Exception as e:
            self.Process.append(f"計算出錯: {e}")