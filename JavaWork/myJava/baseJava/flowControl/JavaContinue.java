/**
* Filename : JavaContinue.java
* Author : DengPengFei
* Creation time : 上午11:53:42 - 2020年5月6日
*/
package flowControl;

/**
 *   continue和break 语句区别：
 *   
 *   break: 当循环执行到break语句时,就退出整个循环,然后执行循环外的语句
 *   continue: 当循环语句执行到continue时,当次循环结束,重新开始下一轮循环
 */

public class JavaContinue {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//test1();
		test2();
		
	}
	
	// continue 判单偶数 跳过输出奇数
	public static void test1() {
		
		for (int i = 0; i < 10; i++) {
			
			if (i < 5) {
				
				continue;
				
			}
			System.out.println(i);
			
		}
		
	}
	
	// continue goto 语句格式
	public static void test2() {
		
		 label1: for (int i = 1; i < 5; i++) {
			for (int j = 1; j < 5; j++) {
				if (i == j) {
					// 跳过 i==y 的坐标
					continue  label1;
				}
				System.out.println(i+","+j);
			}
		}
		
	}

}
