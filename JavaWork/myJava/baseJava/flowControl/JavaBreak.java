/**
* Filename : JavaBreak.java
* Author : DengPengFei
* Creation time : ����5:24:17 - 2020��4��30��
*/
package flowControl;
import java.util.Scanner;

/*
 *    Java �е� break �÷�
 */

public class JavaBreak {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		test1();
		test2();
		test3();
		test4();
		test5();
		
	}
	
	/*
	 * С���μ���һ�� 1000 �׵ĳ��ܱ������� 100 �׵��ܵ��ϣ���ѭ�������ţ�ÿ��һȦ��
	 * ʣ��·�̾ͻ���� 100 �ף�Ҫ�ܵ�Ȧ������ѭ���Ĵ��������ǣ���ÿ����һȦʱ��
	 * �����������Ƿ�Ҫ�����ȥ������ش� y��������ܣ������ʾ����
	 */
	public static void test1() {
		
		Scanner input = new Scanner(System.in);
		
		
		for (int i = 1; i <= 5; i++) {
			
			System.out.println("�ܵ��ǵ�"+i+"Ȧ��");
			System.out.println("�㻹�ܼ����");
			
			String answer = input.next();
			
			// �� ���� yes Ҳ���� ������ yes , java�� ������ == ��ʾ���ַ����� equals ��ʾ
			if (!answer.equals("yes")) {
				System.out.println("������");
				break;
			}
			System.out.println("���ͣ�������");
			if (i == 5) {
				System.out.println("��ϲ�������1000�׵ĳ��ܣ�");
			}
			
		}
//		input.close();
		
	}
	
	// ��дһ�� Java ���������û����� 6 �ſγ̳ɼ������¼��ĳɼ�Ϊ��������ѭ����
	// ���¼�� 6 �źϷ��ɼ�����������гɼ�֮��
	public static void test2() {
		
		// ʵ����
		Scanner input = new Scanner(System.in);
		
		int score = 0;
		
		boolean flag = true; // Ĭ�ϳɼ�����0 Ϊ true
		
		int sum = 0;  // ��ʼ���ɼ��ܺ�Ϊ 0
		
		for (int i = 1; i < 7; i++) {
			
			System.out.println("���������ĵ�"+i+"�Ƴɼ���");
			
			score = input.nextInt();
			
			if (score < 0) {
				// �ɼ���ʽ����
				flag = false;
				break;
				
			}
			sum += score;
				
		}
		
		input.close();
		
		// ����ܳɼ�
		if (flag) {
			System.out.println("�����ܳɼ�Ϊ:"+sum);
		}else {
			System.out.printf("������ĳɼ�: "+score+"��ʽ����");
		}
	}
	
	// Ƕ��ѭ��
	public static void test3() {
		
		for (int i = 1; i <= 5; i++) {
			
			System.out.println("��һ��ѭ��"+i);
			
			for (int j = 1; j <=5; j++) {
				
				System.out.println("�ڶ���ѭ��"+j);
				
				if (j == 3) {
					break;
				}
				
			}
			
		}
		
	}
	
	// break �� goto ���� 
	public static void test4() {
		
		System.out.println("break �� goto ���� ");
		
		// ��� label ��ǩ�������е�ѭ������ �������� ���Ƕ��ѭ�� ֱ�ӿ�������ĳ��ѭ��
		label: for (int i = 0; i < 5; i++) {
			
			for (int j = 0; j < 5; j++) {
				
				System.out.println(j);
				
				if (j % 2 != 0) {
					
					// ֱ�Ӵ�label ��ǩ������ѭ��
					break label;
				}
				
			}
			
		}
		
	}
	
	// switch - case �����ʹ�� break goto 
	public static void test5() {
		
		System.out.println("switch - case �����ʹ�� break goto ");
		
		for (int i = 0; i < 10; i++) {
			
			System.out.println(i);
			
			// i == 5 ʱ���� switch ���
			label: switch (i) {
			
			case 5:
				break label;

			default:
				break;
			}
			
		}
		
	}

}
