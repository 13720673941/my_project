/**
* Filename : IfAndElse.java
* Author : DengPengFei
* Creation time : 下午4:51:56 - 2020年4月28日
*/
package flowControl;
import java.util.Scanner;

/*
 *     Java 中 if else 判断语句
 *     
 *     if - else if  和 if - if 前者条件1成功后不判断条件2  后者两个条件互不影响都进行判断
 *     
 */

public class JavaIfElse {
	
	public static void test1() {
		
		// 编写一个 Java 程序，允许用户从键盘输入一个数字，再判断该数是否大于 100。
		System.out.println("请输入一个数字：");
		Scanner input = new Scanner(System.in);
		// 接受输入收据
		int number = input.nextInt();
		// 判断语句
		if (number > 100) {
			System.out.printf("您输入的数字：%d > 100 ",number);
		}
		if (number < 100) {
			System.out.printf("您输入的数字：%d < 100 ",number);
		}else {
			System.out.printf("请重新输入一个整数！");
		}
//		input.close();
		
	}
	
	public static void test2() {
		
		// 活动计划安排，如果今天是工作日，去上班；如果今天是周末，则出去游玩；同时，如果周末天气晴朗，去室外游乐场游玩，否则去室内游乐场游玩
		
		String today = "周一";
	    String weather = "晴朗";
	    if (today == "周末") {
	        if (weather.equals("晴朗")) {
	            System.out.println("\n去室外游乐场游玩");
	        } else {
	            System.out.println("\n去室内游乐场游玩");
	        }
	    } else {
	        System.out.println("\n去上班");
	    }
		
	}
	
	public static void test3() {
		
		System.out.println("请输入您的考试分数：");
		
		Scanner inputScore = new Scanner(System.in);
		
		int score = inputScore.nextInt();
		
		// 成绩的判断标准是：不低于 90，优秀；低于 90 但不低于 80，良好；低于 80 但不低于 60，中等；否则评为差
		if (score >= 90) {
			System.out.printf("您的成绩：%d 优秀 ！",score);
		}else if (score < 90 && score >= 80) {
			System.out.printf("您的成绩：%d 良好 ！",score);
		}else if (score < 80 && score >= 60) {
			System.out.printf("您的成绩：%d 中等 ！",score);
		}else {
			System.out.printf("您的成绩：%d 很差 ！",score);
		}
		inputScore.close();
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		test1();
		test2();
		test3();
		
	}

}
