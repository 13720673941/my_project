/**
* Filename : JavaWhile.java
* Author : DengPengFei
* Creation time : ����9:33:12 - 2020��4��30��
*/
package flowControl;

/*
 *   Java �е�while��� do-while ѭ�������ص�����ִ��ѭ���壬Ȼ���ж�ѭ�������Ƿ����
 *   
 *   while ѭ���� do-while ѭ���Ĳ�ͬ�����£�
 *   �﷨��ͬ���� while ѭ����ȣ�do-while ѭ���� while �ؼ��ֺ�ѭ���������ں��棬����ǰ����� do �ؼ��֣��������һ���ֺ�
 *   ִ�д���ͬ��while ѭ�����жϣ���ִ�С�do-while ѭ����ִ�У����жϡ�
 *   һ��ʼѭ�������Ͳ����������£�while ѭ��һ�ζ�����ִ�У�do-while ѭ���򲻹�ʲô����¶�����ִ��һ�Ρ�
 */

public class JavaWhile {
	
	// while ѭ�����
	public static void test1() {
		
		int number = 1;
		
		while (number < 10) {
			
			System.out.println("��������");
			
			number ++;
			
		}
		
	}

	// do - while ѭ�����
	public static void test2() {
		
		int number = 1,result = 1;
	    do {
	        result*=number;
	        number++;
	    }while(number <= 10);
	    
	    System.out.print("10�׳˽���ǣ�"+result+"\n");
		
	}
	
	// ��һ��ͼ��ϵͳ���Ƽ�ͼ���б��б����� 50 ����Ϣ��������Ҫ����ÿ����ʾ 10 ������ 5 �н�����ʾ������ʹ�� do-while ѭ�������ʵ�����Ч��
	public static void test3() {
		
		int bookIndex = 1;
		
		do {
			
			// print ��׼��� ������ 
			System.out.print(bookIndex+"\t");
			
			if (bookIndex%10==0) {
				System.out.println();
			}
			
			bookIndex++;
			
		} while (bookIndex < 101);
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		test1();
		test2();
		test3();

	}

}
