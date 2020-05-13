/**
* Filename : IfAndElse.java
* Author : DengPengFei
* Creation time : ����4:51:56 - 2020��4��28��
*/
package flowControl;
import java.util.Scanner;

/*
 *     Java �� if else �ж����
 *     
 *     if - else if  �� if - if ǰ������1�ɹ����ж�����2  ����������������Ӱ�춼�����ж�
 *     
 */

public class JavaIfElse {
	
	public static void test1() {
		
		// ��дһ�� Java ���������û��Ӽ�������һ�����֣����жϸ����Ƿ���� 100��
		System.out.println("������һ�����֣�");
		Scanner input = new Scanner(System.in);
		// ���������վ�
		int number = input.nextInt();
		// �ж����
		if (number > 100) {
			System.out.printf("����������֣�%d > 100 ",number);
		}
		if (number < 100) {
			System.out.printf("����������֣�%d < 100 ",number);
		}else {
			System.out.printf("����������һ��������");
		}
//		input.close();
		
	}
	
	public static void test2() {
		
		// ��ƻ����ţ���������ǹ����գ�ȥ�ϰࣻ�����������ĩ�����ȥ���棻ͬʱ�������ĩ�������ʣ�ȥ�������ֳ����棬����ȥ�������ֳ�����
		
		String today = "��һ";
	    String weather = "����";
	    if (today == "��ĩ") {
	        if (weather.equals("����")) {
	            System.out.println("\nȥ�������ֳ�����");
	        } else {
	            System.out.println("\nȥ�������ֳ�����");
	        }
	    } else {
	        System.out.println("\nȥ�ϰ�");
	    }
		
	}
	
	public static void test3() {
		
		System.out.println("���������Ŀ��Է�����");
		
		Scanner inputScore = new Scanner(System.in);
		
		int score = inputScore.nextInt();
		
		// �ɼ����жϱ�׼�ǣ������� 90�����㣻���� 90 �������� 80�����ã����� 80 �������� 60���еȣ�������Ϊ��
		if (score >= 90) {
			System.out.printf("���ĳɼ���%d ���� ��",score);
		}else if (score < 90 && score >= 80) {
			System.out.printf("���ĳɼ���%d ���� ��",score);
		}else if (score < 80 && score >= 60) {
			System.out.printf("���ĳɼ���%d �е� ��",score);
		}else {
			System.out.printf("���ĳɼ���%d �ܲ� ��",score);
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
