package designBase;

/*
 *    		��������ת��
 */

public class dataConversion {
	
	// ���� 1 ��ʽת�����Զ�����ת����
	public static void uageOne() {
		/*
		 * ������� 2 �����������㣬��ô��һ�����͵����ݸ�������һ�����ͱ�����ʱ����ִ���Զ�����ת����automatic type conversion����
		 * 	�����������ͱ˴˼���
		 * 	Ŀ�����͵�ȡֵ��Χ����Դ�������ͣ��ͼ���������ת���ɸ߼��������ݣ�
		 * ����������У����ڲ�ͬ���������ͻ�ת����ͬһ���������ͣ��������͡��������Լ��ַ��Ͷ����Բ��������㡣�Զ�ת���Ĺ����Ǵӵͼ���������
		 * ת���ɸ߼��������ݡ�ת���������£�
		 * ��ֵ�����ݵ�ת����byte��short��int��long��float��double��
		 * �ַ���ת��Ϊ���ͣ�char��int��
		 */
		
		// �˿͵����й���������� 2 �У����ֽ 4 �С���������ļ۸��� 10.9 Ԫ�����ֽ�ļ۸��� 5.8 Ԫ������Ʒ�ܼ۸�ʵ�ִ�������
		
		float price1 = 10.9f; // ��������ļ۸�
	    double price2 = 5.8; // �������ֽ�ļ۸�
	    int num1 = 2; // �������������
	    int num2 = 4; // �������ֽ������
	    double res = price1 * num1 + price2 * num2; // �����ܼ�
	    System.out.println("һ����������Ա" + res + "Ԫ"); // ����ܼ�
		
	}
	
	// ��ʽת����ǿ������ת����
	public static void uageTwo() {
		
	    float price1 = 10.9f;
	    double price2 = 5.8;
	    int num1 = 2;
	    int num2 = 4;
	    int res2 = (int) (price1 * num1 + price2 * num2);
	    System.out.println("һ����������Ա" + res2 + "Ԫ");
	    
	    int number = 2;
	    // ת���ַ���
	    String money = String.valueOf(number);
	    System.out.println("����ת���ַ�����" + money);
		
	}
	
	// ��main������ִ�г��� ���� python�е�mian����
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		uageOne();
		uageTwo();
	}

}