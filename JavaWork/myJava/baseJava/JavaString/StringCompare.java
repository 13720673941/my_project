/**
* Filename : StringCompare.java
* Author : DengPengFei
* Creation time : ����4:49:32 - 2020��5��10��
*/
package JavaString;

import java.util.Scanner;

/*
 *   Java ���ַ����ıȽ�  equals ...
 *   
 *   �� Java �У��Ƚ��ַ����ĳ��÷����� 3 ����equals() ������equalsIgnoreCase() ������ compareTo() ����
 */

public class StringCompare {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo3();
		demo1();
		demo2();
		
	}
	
	// equals() ����: ����رȽ������ַ�����ÿ���ַ��Ƿ���ͬ����������ַ���������ͬ���ַ��ͳ���,�����ַ��Ĵ�Сд��Ҳ�ڼ��ķ�Χ֮��
	public static void demo1() {
		
		/*
		 *  �ڵ�һ�ν���ϵͳʱҪ�����Ա����һ�����룬���ڰ�ȫ����������Ҫ�������Σ�����������������һ�²���Ч��������ʾʧ��
		 */
		
		System.out.println("��ӭ���롶ѧ����Ϣ����ϵͳ");
		Scanner input = new Scanner(System.in);
		System.out.println("���������룺");
		// ��ȡ���������ֶ�
		String loginPassword = input.next();
		System.out.println("��ȷ���������룺");
		// ��ȡ����ڶ����ֶ�
		String confirmPassword = input.next();
		// �ж��������������Ƿ�һ��
		if (loginPassword.equals(confirmPassword)) {
			System.out.println("�������óɹ���");
		}else {
			System.out.println("��ȷ����������һ�£�");
		}
		
	}
	
	// equalsIgnoreCase() ����: ���﷨�� equals() ������ȫ��ͬ��Ψһ��ͬ���� equalsIgnoreCase() �Ƚ�ʱ�����ִ�Сд
	public static void demo2() {
		
		/*
		 * �ڻ�Աϵͳ����Ҫ�����û�����������м��飬����ʹ�� equalsIgnoreCase() ����ʵ�ּ����¼ʱ�������û���������Ĵ�Сд
		 */
		
		System.out.println("��ӭ���롶ѧ����Ϣ����ϵͳ");
		Scanner input = new Scanner(System.in);
		System.out.println("�������û�����");
		// ��ȡ���������ֶ�
		String username = input.next();
		System.out.println("���������룺");
		// ��ȡ����ڶ����ֶ�
		String password = input.next();
		// �ж��˺�������Ϣ
		if (username.equalsIgnoreCase("admin") && password.equalsIgnoreCase("admincjsh")) {
			System.out.println("��¼�ɹ���");
		}else {
			System.out.println("�û��������벻��ȷ��");
		}
		input.close();
		
	}
	
	// compareTo() ����: ���ᰴ�ֵ�˳�� str ��ʾ���ַ������� otherstr ������ʾ���ַ����н��бȽ�
	// ������ֵ�˳�� str λ�� otherster ����֮ǰ���ȽϽ��Ϊһ������������� str λ�� otherstr ֮�󣬱ȽϽ��Ϊһ������������������ַ�����ȣ�����Ϊ 0
	public static void demo3() {
		
		String str = "A";
	    String str1 = "a";
	    System.out.println("str=" + str);
	    System.out.println("str1=" + str1);
	    System.out.println("str.compareTo(str1)�Ľ���ǣ�" + str.compareTo(str1));
	    System.out.println("str1.compareTo(str)�Ľ���ǣ�" + str1.compareTo(str));
	    System.out.println("str1.compareTo('a')�Ľ���ǣ�" + str1.compareTo("a"));
		
	}
	
}
