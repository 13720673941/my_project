/**
* Filename : Uage_CheckFileNameEM.java
* Author : DengPengFei
* Creation time : 上午9:21:35 - 2020年5月11日
*/
package JavaString;
import java.util.Scanner;

public class Uage_CheckFileNameEM {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		
	}
	
	public static void demo1() {
		
		/*
		 * 假设，在作业提交系统中学生需要录入提交的 Java 文件名称及要提交到的邮箱地址，
		 * 那么就需要对学生输入的这些信息进行校验，判断输入是否有误。
		 * 校验的规则为：录入的文件名称必须以“.java”结尾，录入的邮箱地址中必须包含有“@”符号和“.”符号，且“@”在“.”之前。
		 * 
		 */
		
		Scanner input = new Scanner(System.in);
		System.out.println("********** 【欢迎登录作业提交系统】 **********");
		// 输入文件名称
		System.out.println("请输入作业名称：");
		// 获取输入信息
		String name = input.next();
		// 输入邮箱地址
		System.out.println("请输入邮箱地址：");
		// 获取输入信息
		String email = input.next();
		
		// 定义变量文件名和邮箱地址
		boolean nameCon = false;
		boolean emailCon = false;
		
		// 获取文件名中 . 的索引值
		int index = name.indexOf(".java");
		// 判断文件名称  *** 单个字符要使用单引号
		if (index != -1) {
			if (name.charAt(index+1) == 'j' && name.charAt(index+2) == 'a' && 
					name.charAt(index+3) == 'v' && name.charAt(index+4) == 'a') {
				nameCon = true;
			}
		}else {
			nameCon = false;
		}
		// 判断邮箱地址
		int index1 = email.indexOf('@');
		int index2 = email.indexOf('.');
		if (index1 != -1 && index2 != -1 && index1 < index2) {
			emailCon = true;
		}else {
			emailCon = false;
		}
		// 判断是否提交成功
		if (nameCon && emailCon) {
			System.out.println("作业提交成功！");
		}else {
			if (nameCon) {
				System.out.println("邮箱地址格式错误！");
			}else if (emailCon) {
				System.out.println("文件名称格式错误！");
			}else {
				System.out.println("文件名称或邮箱地址格式错误！");
			}
		}
		input.close();
		
	}

}
