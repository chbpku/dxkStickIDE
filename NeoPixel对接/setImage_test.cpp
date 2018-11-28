/*
示例：setI与seIC命令读取方式
先假装有这么几个东西：

全局变量
unsigned char buffer[100][3]：用于组装图片的临时变量数组

函数或宏
int GROUP_OFFSET(g)：返回组号在颜色数组内对应的起始灯珠位置
char NGROUP：返回总组数
void SET_RGB(n)：将rgb数组内第n位颜色更新至NeoPixel灯带
bool IS_SQUARE(g)：判断g组是否为9*9方形
bool IS_CIRCLE(g)：判断g组是否为环形
int max(a,b)：返回最大值
int min(a,b)：返回最小值
*/

#define COMMAND_SIZE 4
#define SQUARE_SIZE 9
#define LINE_SIZE 30
#define CIRCLE_SIZE 24

//setI命令使用的数据流处理
void parser_setI(string &command)
{
    int command_size = command.length(); //命令总长度
    if (command_size < COMMAND_SIZE + 5) //至少接收一位图片内像素
        return;
    char group = command[COMMAND_SIZE];                                //分组
    char x = command[COMMAND_SIZE + 1], y = command[COMMAND_SIZE + 2]; //左上角对齐横纵坐标
    char mode = command[COMMAND_SIZE + 3];                             //叠加模式
    if (group < 0 || group >= NGROUP)                                  //组号需在有效范围内
        return;
    int img_width = 0;   //用于记录图片宽
    int buffer_size = 0; //记录缓冲区大小

    //读取图片至缓冲区
    for (int i = 8; i < command_size; i++)
    {
        char c = command[i];
        if ('0' <= c && c <= '9')
        {
            int *tmp = buffer[buffer_size++];
            tmp[0] = tmp[1] = tmp[2] = (c - '0') * 11; //映射图片亮度0-9至白色亮度0-99
            continue;
        }
        if (!img_width) // 以第一行决定图片宽度
            img_width = buffer_size;
        if (c != ':') //非冒号则跳出
            break;
    }

    //应用缓冲区内容
    apply_image(group, x, y, mode, img_width, buffer_size);
}

//seIC命令使用的数据流处理
void parser_seIC(string &command)
{
    int command_size = command.length(); //命令总长度
    if (command_size < COMMAND_SIZE + 5) //至少接收一位图片内像素
        return;
    char group = command[COMMAND_SIZE];                                //分组
    char x = command[COMMAND_SIZE + 1], y = command[COMMAND_SIZE + 2]; //左上角对齐横纵坐标
    char mode = command[COMMAND_SIZE + 3];                             //叠加模式
    if (group < 0 || group >= NGROUP)                                  //组号需在有效范围内
        return;
    int img_width = 0;   //用于记录图片宽
    int buffer_size = 0; //记录缓冲区大小

    //读取图片至缓冲区（3通道）
    int i = 8;
    for (int x = 0; x < 3; x++)
    {
        for (; i < command_size; i++)
        {
            char c = command[i];
            if ('0' <= c && c <= '9')
            {
                int *tmp = buffer[buffer_size++];
                tmp[x] = (c - '0') * 11; //映射图片亮度0-9至RGB亮度0-99
                continue;
            }
            if (!img_width) // 以第一行决定图片宽度
                img_width = buffer_size;
            if (c != ':') //非冒号则跳出
            {
                i++; //跳过图片间分隔符
                break;
            }
        }
    }

    //应用缓冲区内容
    apply_image(group, x, y, mode, img_width, buffer_size);
}

//将缓冲区内容添加至灯带
void apply_image(char group, char x, char y, char mode, int img_width, int buffer_size)
{
    //填充图片至灯珠链
    int begin = GROUP_OFFSET(group); //获取起始位置
    if (IS_SQUARE(group))            //方形填充
    {
        int xmin = max(0, x), xmax = min(SQUARE_SIZE, img_width); //横坐标遍历范围
        for (int bstart = 0, yptr = max(0, y);                    //分别用于遍历缓冲区与逐行遍历图片
             bstart + img_width <= buffer_size && yptr < SQUARE_SIZE;
             bstart += img_width, yptr++)
        {
            for (int xptr = xmin; xptr < xmax; xptr++)
            {
                /* 计算灯珠串内位置
                以下两行保留一行，若y正坐标向上则将yptr替换为(SQUARE_SIZE-yptr)，若x正坐标向左则将xptr替换为(SQUARE_SIZE-xptr) */
                int pos = begin + yptr * SQUARE_SIZE + xptr; //逐行排列
                int pos = begin + xptr * SQUARE_SIZE + yptr; //逐列排列
                int bptr = bstart + xptr - x;                //计算缓冲区内位置

                if (mode) //相加模式
                    for (int i = 0; i < 3; i++)
                        rgb[pos][i] = min(255, rgb[pos][i] + buffer[bptr][i]);
                else //覆盖模式
                    for (int i = 0; i < 3; i++)
                        rgb[pos][i] = buffer[bptr][i];

                SET_RGB(pos); //更新至灯带
            }
        }
    }
    else //线性填充，将图片展平为一维填入
    {
        int offset_start, offset_end, group_size;
        if (IS_CIRCLE(group)) // 环形：取最大为环形长度的颜色
        {
            offset_start = 0;
            offset_end = min(buffer_size, CIRCLE_SIZE);
            group_size = CIRCLE_SIZE;
        }
        else //线状：根据最值截尾
        {
            offset_start = max(0, -x);
            offset_end = min(buffer_size, LINE_SIZE);
            group_size = LINE_SIZE;
        }
        for (int bptr = offset_start; bptr < offset_end; bptr++)
        {
            int pos = begin + (x + bptr) % group_size;
            if (mode) //相加模式
                for (int i = 0; i < 3; i++)
                    rgb[pos][i] = min(255, rgb[pos][i] + buffer[bptr][i]);
            else //覆盖模式
                for (int i = 0; i < 3; i++)
                    rgb[pos][i] = buffer[bptr][i];

            SET_RGB(pos); //更新至灯带
        }
    }
}