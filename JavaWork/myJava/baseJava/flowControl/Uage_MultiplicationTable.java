/**
* Filename : Uage_MultiplicationTable.java
* Author : DengPengFei
* Creation time : ����2:57:52 - 2020��4��30��
*/
package flowControl;

/*
 *   ���� for ѭ��Ƕ����� 99�˷��� 
 */

public class Uage_MultiplicationTable {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		test1();
		
	}
	
	public static void test1() {
		
		System.out.println("�˷��ھ���");
		
		for (int i = 1; i < 10; i++) {
			for (int j = 1; j <= i; j++) {
				System.out.printf("%d x %d = %d"+"\t",j,i,i*j);
			}
			System.out.println();
			
		}
		
	}

}
