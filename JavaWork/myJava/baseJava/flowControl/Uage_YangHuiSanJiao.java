/**
* Filename : Uage_YangHuiSanJiao.java
* Author : DengPengFei
* Creation time : ����5:46:12 - 2020��5��8��
*/
package flowControl;

public class Uage_YangHuiSanJiao {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// System.out.println(num(5,2));
		create(10);
	}
	
	// ���
	public static int num(int x, int y) {
		
		// ���һ�к����һ�е����� ����1 
		if (y == 1 || x == y) {
			return 1;
		}else {
			// ���㵱ǰ���ֺ�(��һ�м����ͱ���������������)
			int z = num(x - 1, y - 1) + num(x - 1, y);
			return z;
		}

	}

	public static void create(int row) {
		
		// ѭ����
		for (int i = 1; i <= row; i++) {
			
			// ��ӡÿ��ǰ��Ŀո�
			for (int j = 1; j <= row-i; j++) {
				System.out.print(" ");
			}
			// ��ӡ����
			for (int j = 1; j <= i; j++) {
				System.out.print(num(i,j)+" ");
			}
			// ѭ��һ�л���
			System.out.println();
		}
		
	}
	
}
