/**
* Filename : StrPatternAndMatcher.java
* Author : DengPengFei
* Creation time : 上午9:48:00 - 2020年5月21日
*/
package JavaString;

import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/*
 *   Java 正则表达式
 */

public class StrPatternAndMatcher {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println("--------- demo1 ----------");
		demo1();
		System.out.println("--------- demo2 ----------");
		demo2();
		System.out.println("--------- demo3 ----------");
		demo3();
		System.out.println("--------- demo4 ----------");
		demo4();
		
	}
	
	// find() 方法: 返回目标字符串中是否包含与 Pattern 匹配的子串
	public static void demo1() {
		
		String str = "我想找一套适合自己的JAVA教程，尽快联系我13500006666" + "交朋友，电话号码是13611125565" + "出售二手电脑，联系方式15899903312";
		
		// 创建一个Pattern对象，并用它建立一个Matcher对象
        // 该正则表达式只抓取13X和15X段的手机号
        // 实际要抓取哪些电话号码，只要修改正则表达式即可
		
		Pattern p = Pattern.compile("\\d{11}");

		Matcher m = p.matcher(str);
		
		while (m.find()) {
            System.out.println(m.group());
		
		}
		
	}
	
	// start() 和 end() 方法 开始和结束位置索引
	public static void demo2() {
		
		// 创建一个Pattern对象，并用它建立一个Matcher对象
        String str = "Java is very easy!";
        
        Pattern p = Pattern.compile("\\w+");
        
        Matcher m = p.matcher(str);
        
        while (m.find()) {
        	System.out.println("查找字符串："+m.group()+"开始位置："+m.start()+"结束位置："+m.end());
		}
		
	}
	
	// matcher.matches() 当所有正则匹配时返回 true 否则返回 false
	public static void demo3() {
		
		String[] mails = { "kongyeeku@163.com", "kongyeeku@gmail.com", "ligang@crazyit.org", "wawa@abc.xx", "908066950@qq.com"};
        
		Pattern pattern = Pattern.compile("((\\w{3,20})|(\\d{3,20}))@\\w+\\.(com|org)");
		
		for (String mail : mails) {
			
			Matcher matcher = pattern.matcher(mail);
			
			// matcher.matches() 当所有正则匹配时返回 true 否则返回 false
			// lookingAt() 方法只匹配开头匹配/不匹配直接就false 进行匹配下一个
			System.out.println("邮箱："+mail+(matcher.matches() ? "是":"不是")+"一个有效的邮箱地址！");
		}
		
	}
	
	// 利用正则表达式对目标字符串进行分割、查找、替换等操作
	public static void demo4() {
		
		String[] message = { "Java has regular expressions in 1.4", "regular expressions now expressing in Java",
				"Java represses oracular expressions" };
		
		// 创建正则表达式
		Pattern pattern = Pattern.compile("re\\w+");
		
		for (int i = 0; i < message.length; i++) {
			
			Matcher matcher = pattern.matcher(message[i]);
			
			System.out.println(matcher.replaceAll("AAAAA"));
			
			System.out.println(matcher.replaceFirst("BBBBB"));
			
			System.out.println(Arrays.toString(message[i].split(" ")));
			
		}
		
	}
	
	
}


