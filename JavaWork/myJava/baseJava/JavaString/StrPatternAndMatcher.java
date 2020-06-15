/**
* Filename : StrPatternAndMatcher.java
* Author : DengPengFei
* Creation time : ����9:48:00 - 2020��5��21��
*/
package JavaString;

import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/*
 *   Java ������ʽ
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
	
	// find() ����: ����Ŀ���ַ������Ƿ������ Pattern ƥ����Ӵ�
	public static void demo1() {
		
		String str = "������һ���ʺ��Լ���JAVA�̳̣�������ϵ��13500006666" + "�����ѣ��绰������13611125565" + "���۶��ֵ��ԣ���ϵ��ʽ15899903312";
		
		// ����һ��Pattern���󣬲���������һ��Matcher����
        // ��������ʽֻץȡ13X��15X�ε��ֻ���
        // ʵ��Ҫץȡ��Щ�绰���룬ֻҪ�޸�������ʽ����
		
		Pattern p = Pattern.compile("\\d{11}");

		Matcher m = p.matcher(str);
		
		while (m.find()) {
            System.out.println(m.group());
		
		}
		
	}
	
	// start() �� end() ���� ��ʼ�ͽ���λ������
	public static void demo2() {
		
		// ����һ��Pattern���󣬲���������һ��Matcher����
        String str = "Java is very easy!";
        
        Pattern p = Pattern.compile("\\w+");
        
        Matcher m = p.matcher(str);
        
        while (m.find()) {
        	System.out.println("�����ַ�����"+m.group()+"��ʼλ�ã�"+m.start()+"����λ�ã�"+m.end());
		}
		
	}
	
	// matcher.matches() ����������ƥ��ʱ���� true ���򷵻� false
	public static void demo3() {
		
		String[] mails = { "kongyeeku@163.com", "kongyeeku@gmail.com", "ligang@crazyit.org", "wawa@abc.xx", "908066950@qq.com"};
        
		Pattern pattern = Pattern.compile("((\\w{3,20})|(\\d{3,20}))@\\w+\\.(com|org)");
		
		for (String mail : mails) {
			
			Matcher matcher = pattern.matcher(mail);
			
			// matcher.matches() ����������ƥ��ʱ���� true ���򷵻� false
			// lookingAt() ����ֻƥ�俪ͷƥ��/��ƥ��ֱ�Ӿ�false ����ƥ����һ��
			System.out.println("���䣺"+mail+(matcher.matches() ? "��":"����")+"һ����Ч�������ַ��");
		}
		
	}
	
	// ����������ʽ��Ŀ���ַ������зָ���ҡ��滻�Ȳ���
	public static void demo4() {
		
		String[] message = { "Java has regular expressions in 1.4", "regular expressions now expressing in Java",
				"Java represses oracular expressions" };
		
		// ����������ʽ
		Pattern pattern = Pattern.compile("re\\w+");
		
		for (int i = 0; i < message.length; i++) {
			
			Matcher matcher = pattern.matcher(message[i]);
			
			System.out.println(matcher.replaceAll("AAAAA"));
			
			System.out.println(matcher.replaceFirst("BBBBB"));
			
			System.out.println(Arrays.toString(message[i].split(" ")));
			
		}
		
	}
	
	
}


