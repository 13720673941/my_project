/**
* Filename : GetStringLenght.java
* Author : DengPengFei
* Creation time : ����3:36:31 - 2020��5��9��
*/
package JavaString;
import java.util.Scanner;

/*
 *   ��ȡ�ַ����ĳ���
 */

public class GetStringLenght {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();

	}
	
	public static void demo1() {
		
		/*
		 * ��ѧ����Ϣ����ϵͳ�жԹ���Ա�����������Ĺ涨�������볤�ȱ������ 6 λ��С�� 12 λ����Ϊ����̫�����ױ��ƽ⣬̫���Ļ��ֲ����׼�ס��
		 * �����Ҫ���Ȼ�ȡ�û�����������ַ�����Ȼ����� length() ������ȡ���ȣ�������һ���ĳ����жϣ�����ʵ�ִ���������ʾ
		 */
		
		System.out.println("��ӭ���롶ѧ����Ϣ����ϵͳ");// ���ϵͳ����
		
		Scanner input = new Scanner(System.in);
		
		System.out.println("������һ������Ա���룺");
		String password = input.next();
		
		// ��ȡ������ַ������� int ����
		int passLength = password.length();
		// �ж��ַ�����
		if (passLength < 12 && passLength > 6) {
			System.out.println("����������볤����ȷ��");
		}else if (passLength >= 12) {
			System.out.println("����������������");
		}else {
			System.out.println("�������������̣�");
		}
		input.close();
		
	}

}
