/**
* Filename : Uage_YangHuiSanJiao.java
* Author : DengPengFei
* Creation time : 下午5:46:12 - 2020年5月8日
*/
package flowControl;

public class Uage_YangHuiSanJiao {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// System.out.println(num(5,2));
		create(10);
	}
	
	// 求和
	public static int num(int x, int y) {
		
		// 求第一列和最后一列的数字 都是1 
		if (y == 1 || x == y) {
			return 1;
		}else {
			// 计算当前数字和(上一行加数和被加数的数字坐标)
			int z = num(x - 1, y - 1) + num(x - 1, y);
			return z;
		}

	}

	public static void create(int row) {
		
		// 循环行
		for (int i = 1; i <= row; i++) {
			
			// 打印每行前面的空格
			for (int j = 1; j <= row-i; j++) {
				System.out.print(" ");
			}
			// 打印数字
			for (int j = 1; j <= i; j++) {
				System.out.print(num(i,j)+" ");
			}
			// 循环一行换行
			System.out.println();
		}
		
	}
	
}
