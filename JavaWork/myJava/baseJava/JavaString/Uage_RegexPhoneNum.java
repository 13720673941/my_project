/**
* Filename : Uage_RegexPhoneNum.java
* Author : DengPengFei
* Creation time : ����3:58:01 - 2020��5��21��
*/
package JavaString;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.print.DocFlavor.INPUT_STREAM;

/*
 *   Java ��������ƥ���ж�������ֻ����Ƿ���ȷ
 */

public class Uage_RegexPhoneNum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		// �����ֻ���������ʽ  ǰ������������������� + - �� �ո� + �绰�� ����������13 15��ͷ���ֻ���
		String regex = "0\\d{2,3}[-]?\\d{7,8}|0\\d{2,3}s?\\d{7,8}|13[0-9]\\d{8}|15[1089]\\d{8}";
		
		// Ĭ�ϼ��� Y
		String isContinue = "Y";
		
		do {
			Scanner input = new Scanner(System.in);
			// �����ֻ���
			System.out.println("�����������ֻ��ţ�");
			String phoneNumber = input.next();
			Pattern pattern = Pattern.compile(regex);
			Matcher matcher = pattern.matcher(phoneNumber);
			// ȫ��ƥ�䷵��true
			boolean isOk = matcher.matches();
			if (isOk) {
				System.out.println("������ֻ�������ȷ��");
			}else {
				System.out.println("������ֻ�������Ч��");
			}
			System.out.println("���Ƿ�������룿Y/N");
			isContinue = input.next();
		} while (isContinue.toLowerCase().equals("y"));
			System.out.println("�����˳���....");
	}

}
