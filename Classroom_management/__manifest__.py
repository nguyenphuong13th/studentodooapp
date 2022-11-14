{
    'name':"Classroom_management - phuong.info", #tên module
    'summary':"""My student model""",#mô tả ngắn gọn về module
    'description':"""Managing student infomation""",
    'author':"hoang-phuong",
    'website':"https://studentapp.info",
    'catagory':"Uncategorized",
    'version':"0.1",
    'depends':[
        'product'
    ],# dependency của module mình sẽ phụ thuộc vào những app/module khác nào.product là một module built-in đặc tả khi cài đặt My student sẽ trigger cài đặt product
    'data':[],#liên quan đến view
    'installable':True,
    'application':True, # khi vào menu Apps, mặc định filter "Apps" sẽ được dùng.Nếu application set false => ko hiện ra khi filter "App",ngược lại được xem nh7 1 application.Application False khi module này là như một module kỹ thuật phụ trợ
    'data': [
        'security/ir.model.access.csv',
        'views/my_student_views.xml',

    ],


}