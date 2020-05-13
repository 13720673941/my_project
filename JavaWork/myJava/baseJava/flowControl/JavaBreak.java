/**
* Filename : JavaBreak.java
* Author : DengPengFei
* Creation time : 下午5:24:17 - 2020年4月30日
*/
package flowControl;
import java.util.Scanner;

/*
 *    Java 中的 break 用法
 */

public class JavaBreak {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		test1();
		test2();
		test3();
		test4();
		test5();
		
	}
	
	/*
	 * 小明参加了一个 1000 米的长跑比赛，在 100 米的跑道上，他循环地跑着，每跑一圈，
	 * 剩余路程就会减少 100 米，要跑的圈数就是循环的次数。但是，在每跑完一圈时，
	 * 教练会问他是否要坚持下去，如果回答 y，则继续跑，否则表示放弃
	 */
	public static void test1() {
		
		Scanner input = new Scanner(System.in);
		
		
		for (int i = 1; i <= 5; i++) {
			
			System.out.println("跑的是第"+i+"圈！");
			System.out.println("你还能坚持吗？");
			
			String answer = input.next();
			
			// 非 等于 yes 也就是 不等于 yes , java中 数字用 == 表示，字符串用 equals 表示
			if (!answer.equals("yes")) {
				System.out.println("放弃！");
				break;
			}
			System.out.println("加油！继续！");
			if (i == 5) {
				System.out.println("恭喜你完成了1000米的长跑！");
			}
			
		}
//		input.close();
		
	}
	
	// 编写一个 Java 程序，允许用户输入 6 门课程成绩，如果录入的成绩为负则跳出循环；
	// 如果录入 6 门合法成绩，则计算已有成绩之和
	public static void test2() {
		
		// 实例化
		Scanner input = new Scanner(System.in);
		
		int score = 0;
		
		boolean flag = true; // 默认成绩大于0 为 true
		
		int sum = 0;  // 初始化成绩总和为 0
		
		for (int i = 1; i < 7; i++) {
			
			System.out.println("请输入您的第"+i+"科成绩：");
			
			score = input.nextInt();
			
			if (score < 0) {
				// 成绩格式错误
				flag = false;
				break;
				
			}
			sum += score;
				
		}
		
		input.close();
		
		// 输出总成绩
		if (flag) {
			System.out.println("您的总成绩为:"+sum);
		}else {
			System.out.printf("您输入的成绩: "+score+"格式错误！");
		}
	}
	
	// 嵌套循环
	public static void test3() {
		
		for (int i = 1; i <= 5; i++) {
			
			System.out.println("第一层循环"+i);
			
			for (int j = 1; j <=5; j++) {
				
				System.out.println("第二层循环"+j);
				
				if (j == 3) {
					break;
				}
				
			}
			
		}
		
	}
	
	// break 的 goto 功能 
	public static void test4() {
		
		System.out.println("break 的 goto 功能 ");
		
		// 添加 label 标签结束该行的循环程序 ，方便于 多层嵌套循环 直接可以跳出某个循环
		label: for (int i = 0; i < 5; i++) {
			
			for (int j = 0; j < 5; j++) {
				
				System.out.println(j);
				
				if (j % 2 != 0) {
					
					// 直接从label 标签出跳出循环
					break label;
				}
				
			}
			
		}
		
	}
	
	// switch - case 语句中使用 break goto 
	public static void test5() {
		
		System.out.println("switch - case 语句中使用 break goto ");
		
		for (int i = 0; i < 10; i++) {
			
			System.out.println(i);
			
			// i == 5 时结束 switch 语句
			label: switch (i) {
			
			case 5:
				break label;

			default:
				break;
			}
			
		}
		
	}

}
