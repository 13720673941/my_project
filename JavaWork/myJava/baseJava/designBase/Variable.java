package designBase;

/*
 * 			����  �Լ�������������
 */


public class Variable {
	
	/*
	 * ��Ա���������֣��ֱ���ȫ�ֱ����;�̬��������������������ڷ����������֮�⣬�������κ�һ����������������������
	 */
	
	// ȫ�ֱ�����ʵ��������	�� static ����	������.������	ֻҪ���󱻵������ã�ʵ�������ͽ�����
	String name; // ��Ա������ʵ������
    int age; // ��Ա������ʵ������
    
    // ��̬�������������	�� static ����	����.�������������.������	����������ȡ��������������ڡ��౻�������ջ��Ƴ��׻���ʱ�Żᱻ����
    static final String website = "C����������"; // ��Ա��������̬����(�����)
    static String URL = "http://c.biancheng.net"; // ��Ա��������̬����(�����)
	
    // �����������͸�ֵ
	public static void uageOne() {
		
		// ֱ�Ӹ�������ֵ
		int number = 2;
		// �������ٸ�ֵ
		String username;
		username = "������";
		
		System.out.println(username+number);
		
		/*
		 * String username,address,phone,tel;    // �����������
		 * int num1=12,num2=23,result=35;    // ��������ʼ���������
		 */
		
	}
	
	// �ֲ�����
	public static void partVariable() {
		// ��������������
		int num1 = 7;
		
		if (true) {
			// ֻ������if�� ���ƾֲ�����
			int num2 = 4;
			System.out.println("�ֲ�������"+num2);
			System.out.println("ȫ�ֱ�����"+num1);
		}
		
	}
	
	// ��������  numberΪ����
	public static void uageTwo(int number) {
		
		System.out.println("�������Ϊ��"+number);
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		uageOne();
		partVariable();
		uageTwo(10);
		
		// ������Ķ���
    	Variable dc = new Variable();
        // ������.����������ʵ��������ȫ�ֱ�����
        System.out.println(dc.name);
        System.out.println(dc.age);
        
        // ����.���������þ�̬�������������
        System.out.println(Variable.website); // ��̬��������ֱ��ʹ�ã� ����.������  ����
        System.out.println(Variable.URL);
		
	}

}