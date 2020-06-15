/**
* Filename : Uage_RegexPhoneNum.java
* Author : DengPengFei
* Creation time : 下午3:58:01 - 2020年5月21日
*/
package JavaString;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.print.DocFlavor.INPUT_STREAM;

/*
 *   Java 例：正则匹配判断输入的手机号是否正确
 */

public class Uage_RegexPhoneNum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		// 国内手机号正则表达式  前面两个是座机：区域号 + - 或 空格 + 电话号 后面两个是13 15开头的手机号
		String regex = "0\\d{2,3}[-]?\\d{7,8}|0\\d{2,3}s?\\d{7,8}|13[0-9]\\d{8}|15[1089]\\d{8}";
		
		// 默认继续 Y
		String isContinue = "Y";
		
		do {
			Scanner input = new Scanner(System.in);
			// 输入手机号
			System.out.println("请输入您的手机号：");
			String phoneNumber = input.next();
			Pattern pattern = Pattern.compile(regex);
			Matcher matcher = pattern.matcher(phoneNumber);
			// 全部匹配返回true
			boolean isOk = matcher.matches();
			if (isOk) {
				System.out.println("输入的手机号码正确！");
			}else {
				System.out.println("输入的手机号码无效！");
			}
			System.out.println("您是否继续输入？Y/N");
			isContinue = input.next();
		} while (isContinue.toLowerCase().equals("y"));
			System.out.println("正在退出中....");
	}

}
