/**
* Filename : Uage_MultiplicationTable.java
* Author : DengPengFei
* Creation time : 下午2:57:52 - 2020年4月30日
*/
package flowControl;

/*
 *   利用 for 循环嵌套输出 99乘法表 
 */

public class Uage_MultiplicationTable {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		test1();
		
	}
	
	public static void test1() {
		
		System.out.println("乘法口诀表：");
		
		for (int i = 1; i < 10; i++) {
			for (int j = 1; j <= i; j++) {
				System.out.printf("%d x %d = %d"+"\t",j,i,i*j);
			}
			System.out.println();
			
		}
		
	}

}
