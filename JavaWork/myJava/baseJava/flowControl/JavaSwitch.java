/**
* Filename : SwitchCase.java
* Author : DengPengFei
* Creation time : ����6:50:36 - 2020��4��29��
*/
package flowControl;
import java.util.Scanner;

/*
 *   switch - case  ����ʽ   ** case �����Ǻܶ�� �����ظ��� case ֵ�ǲ�����ġ�
 *   
 *   һ������£������ж��������ٵģ�����ʹ�� if ������䣬������ʵ��һЩ���������ж��У����ʹ�� switch ��䡣
 */

public class JavaSwitch {
	
	// switch - case ���
	public static void test1() {
		
		System.out.println("Please enter yes or no :");
		
		Scanner input = new Scanner(System.in);
		
		String inputText = input.next();
		
		// ��ȡ������ַ���
		switch (inputText.toLowerCase()) {
		// ��ֵ���� yes ʱ�� �˳�
		case "yes":
			
			System.out.println("yes !");
			break;
		
		case "no":
			
			System.out.println("no !");
			break;
		
		default:
			break;
		}
		
		input.close();
		
	}
	
	// switch - case Ƕ��
	public static void test2(String name,String sex) {
		
		switch (name) {
		case "������":
			
			switch (sex) {
			case "��":
				System.out.println("Hello ! ������ ");
				break;

			default:
				break;
			}
			break;
		default:
			System.out.println("Hello !"+name+sex);
			break;
		}
			
	}
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		test1();
		test2("������","��");
		
	}

}

