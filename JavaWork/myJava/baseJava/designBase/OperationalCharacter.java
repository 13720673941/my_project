package designBase;
import java.util.Scanner;

/*
 * 			java ������� 
 */

public class OperationalCharacter {
	
	
	// һԪ�����
	public static void testOne() {
		
		int a = 10;
		
		// ���������������ֵת��
		System.out.println("�����'-': -a = "+(-a));
		
		// ��ʹ�����Լӣ� ��һ���Ѿ����ڴ���������Ϊ 11 ��ʵ��������� 10
		System.out.println("�������'++': a = "+ a++);
		
		// �ڶ���ʹ�õ����ڴ��е�ֵ 11 
		System.out.println("�������ʹ��a'++': a = "+ a);
		
		int b = 10;
				
		// ��������ʹ�� ���� python�е� += 
		System.out.println("�����ǰ'++': b = "+ ++b);
		
	}
	
	// ��Ԫ�����
	public static void testTwo() {
		
		// Java ����������������Ĺ����ǽ����������㣬���˾���ʹ�õļӣ�+��������-�����ˣ�*���ͳ���\���⣬����ȡģ���㣨�������ӣ�+��������-�����ˣ�*��������\
		
		// *** �������������˫Ŀ�����������������������������������ȼ��ϣ�*��/���� ������ͬ���㼶�𣬲����� +��-��+��- ������ͬ����
		
		/*
		 * ������������ʱӦע���������㣺
		 * ���ࣨ��������Ҫ����������������������Ϊ���ͣ�����Ϊ�������͡�
         * �����������г������㣬������Ϊ���������������ʵ�����г������㣬����Ϊʵ��
         * ���磺
		 * ��int x=2,y=1; ����ʽ y/x �Ľ���� 0��
		 * ��float x=2.0f; int y=1; ����ʽ y/x �Ľ���� 0.5
		 */
		
		// println ���һ���ַ����������� ĩβ����
		System.out.println("�������㣺");
		
		// printf ����д����� ĩβ������ 
		System.out.printf("1+1=%d \n",1+1);
		System.out.printf("1-1=%d \n",1-1);
		System.out.printf("1*1=%d \n",1*1);
		System.out.printf("1/1=%d \n",1/1);
		// ����ȡ�� �ַ������� %% ��
		System.out.printf("1%%1=%d \n",1%1);
		
		// �������ļӡ������ˡ�����ȡ��
		System.out.println("\n����������������"); 
		
	    System.out.printf("9+4.5f=%f \n", 9 + 4.5f);
	    System.out.printf("9-3.0f=%f \n", 9 - 3.0f);
	    System.out.printf("9*2.5f=%f \n", 9 * 2.5f);
	    System.out.printf("9/3.0f=%f \n", 9 / 3.0f);
	    System.out.printf("9%%4=%f \n", (float)(9%4));
	    
	    // ���ַ��ļӷ��ͼ���
	    System.out.println("\n�ַ�����������"); 
	    System.out.printf("'A'+32=%d \n", 'A' + 32);
	    System.out.printf("'A'+32=%c \n", 'A' + 32);
	    System.out.printf("'a'-'B'=%d \n", 'a' - 'B');
		
	}
	
	// ������ֵ�����
	public static void testThree() {
		
		int a = 1;
		int b = 2;
		a += b; // �൱�� a = a + b
		System.out.println(a);
		a += b + 3; // �൱�� a = a + b + 3
		System.out.println(a);
		a -= b; // �൱�� a = a - b
		System.out.println(a);
		a *= b; // �൱�� a=a*b
		System.out.println(a);
		a /= b; // �൱�� a=a/b
		System.out.println(a);
		a %= b; // �൱�� a=a%b
		System.out.println(a);
		
		double price = 10.25; // ������Ʒ�ĵ��ۣ���ֵΪ10.25
	    double total = 0; // �����ܼ۳�ʼΪ0
	    int count = 2; // ���幺����������ֵΪ2
	    price -= 1.25; // ��ȥ���۵õ���ǰ����
	    count *= 5; // ������Ҫ����10������ԭ��������5��
	    total = price * count; // �ܼ�=��ǰ����*����
	    //%d������ͣ�%f���������  %.2f ��ʾ��������λ
	    System.out.printf("��Ʒ��ǰ�ĵ���Ϊ��%.2f \n", price); 
	    System.out.printf("������Ʒ������Ϊ��%d \n", count); 
	    System.out.printf("�ܼ�Ϊ��%.2f \n", total);
		
	}
	
	// ��Ŀ�����
	public static void testFour() {
		
		/*
		 * int x,y,z;
		 * x = 6,y = 2;
		 * z = x>y ? x-y : x+y;
		 * ������Ҫ���� z ��ֵ������Ҫ�ж� x>y �����ֵ�����Ϊ true��z ��ֵΪ x-y������ z ��ֵΪ x+y�������� x>y ����ʽ���Ϊ true������ z ��ֵΪ 4��
		 */
		
		int x, y, z; // ������������
        System.out.print("������һ������");
        Scanner input = new Scanner(System.in);
        x = input.nextInt(); // ���û�����x��ֵ
        // �ж�x��ֵ�Ƿ����5�������y=x������y=-x
        y = x > 5 ? x : -x;
        // �ж�y��ֵ�Ƿ����x�������z=y������z=5
        z = y > x ? y : 5;
        System.out.printf("x=%d \n", x);
        System.out.printf("y=%d \n", y);
        System.out.printf("z=%d \n", z);
		
        input.close();
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		testOne();
		testTwo();
		testThree();
		testFour();
	}

}