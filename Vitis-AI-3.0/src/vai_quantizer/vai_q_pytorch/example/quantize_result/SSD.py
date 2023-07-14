# GENETARED BY NNDCT, DO NOT EDIT!

import torch
from torch import tensor
import pytorch_nndct as py_nndct

class SSD(py_nndct.nn.NndctQuantModel):
    def __init__(self):
        super(SSD, self).__init__()
        self.module_0 = py_nndct.nn.Module('nndct_const') #SSD::3183
        self.module_1 = py_nndct.nn.Input() #SSD::input_0
        self.module_2 = py_nndct.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[vgg]/ModuleList[0]/input.3
        self.module_3 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/ReLU[vgg]/ModuleList[1]/input.5
        self.module_4 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[vgg]/ModuleList[2]/input.7
        self.module_5 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/ReLU[vgg]/ModuleList[3]/2068
        self.module_6 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #SSD::SSD/MaxPool2d[vgg]/ModuleList[4]/input.9
        self.module_7 = py_nndct.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[vgg]/ModuleList[5]/input.11
        self.module_8 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/ReLU[vgg]/ModuleList[6]/input.13
        self.module_9 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[vgg]/ModuleList[7]/input.15
        self.module_10 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/ReLU[vgg]/ModuleList[8]/2122
        self.module_11 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #SSD::SSD/MaxPool2d[vgg]/ModuleList[9]/input.17
        self.module_12 = py_nndct.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[vgg]/ModuleList[10]/input.19
        self.module_13 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/ReLU[vgg]/ModuleList[11]/input.21
        self.module_14 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[vgg]/ModuleList[12]/input.23
        self.module_15 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/ReLU[vgg]/ModuleList[13]/input.25
        self.module_16 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[vgg]/ModuleList[14]/input.27
        self.module_17 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/ReLU[vgg]/ModuleList[15]/2196
        self.module_18 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=True) #SSD::SSD/MaxPool2d[vgg]/ModuleList[16]/input.29
        self.module_19 = py_nndct.nn.Conv2d(in_channels=256, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[vgg]/ModuleList[17]/input.31
        self.module_20 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/ReLU[vgg]/ModuleList[18]/input.33
        self.module_21 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[vgg]/ModuleList[19]/input.35
        self.module_22 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/ReLU[vgg]/ModuleList[20]/input.37
        self.module_23 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[vgg]/ModuleList[21]/input.39
        self.module_24 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/ReLU[vgg]/ModuleList[22]/2270
        self.module_25 = py_nndct.nn.Module('aten::pow') #SSD::SSD/L2Norm[L2Norm]/2272
        self.module_26 = py_nndct.nn.Module('nndct_sum') #SSD::SSD/L2Norm[L2Norm]/2277
        self.module_27 = py_nndct.nn.Module('aten::sqrt') #SSD::SSD/L2Norm[L2Norm]/2278
        self.module_28 = py_nndct.nn.Add() #SSD::SSD/L2Norm[L2Norm]/3184
        self.module_29 = py_nndct.nn.Module('nndct_elemwise_div') #SSD::SSD/L2Norm[L2Norm]/2282
        self.module_30 = py_nndct.nn.Module('nndct_unsqueeze') #SSD::SSD/L2Norm[L2Norm]/2284
        self.module_31 = py_nndct.nn.Module('nndct_unsqueeze') #SSD::SSD/L2Norm[L2Norm]/2286
        self.module_32 = py_nndct.nn.Module('nndct_unsqueeze') #SSD::SSD/L2Norm[L2Norm]/2288
        self.module_33 = py_nndct.nn.expand_as() #SSD::SSD/L2Norm[L2Norm]/2289
        self.module_34 = py_nndct.nn.Module('nndct_elemwise_mul') #SSD::SSD/L2Norm[L2Norm]/input.77
        self.module_35 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #SSD::SSD/MaxPool2d[vgg]/ModuleList[23]/input.41
        self.module_36 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[vgg]/ModuleList[24]/input.43
        self.module_37 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/ReLU[vgg]/ModuleList[25]/input.45
        self.module_38 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[vgg]/ModuleList[26]/input.47
        self.module_39 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/ReLU[vgg]/ModuleList[27]/input.49
        self.module_40 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[vgg]/ModuleList[28]/input.51
        self.module_41 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/ReLU[vgg]/ModuleList[29]/2364
        self.module_42 = py_nndct.nn.MaxPool2d(kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], ceil_mode=False) #SSD::SSD/MaxPool2d[vgg]/ModuleList[30]/input.53
        self.module_43 = py_nndct.nn.Conv2d(in_channels=512, out_channels=1024, kernel_size=[3, 3], stride=[1, 1], padding=[6, 6], dilation=[6, 6], groups=1, bias=True) #SSD::SSD/Conv2d[vgg]/ModuleList[31]/input.55
        self.module_44 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/ReLU[vgg]/ModuleList[32]/input.57
        self.module_45 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=1024, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[vgg]/ModuleList[33]/input.59
        self.module_46 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/ReLU[vgg]/ModuleList[34]/input.61
        self.module_47 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[extras]/ModuleList[0]/2437
        self.module_48 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/input.63
        self.module_49 = py_nndct.nn.Conv2d(in_channels=256, out_channels=512, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[extras]/ModuleList[1]/2457
        self.module_50 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/input.65
        self.module_51 = py_nndct.nn.Conv2d(in_channels=512, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[extras]/ModuleList[2]/2477
        self.module_52 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/input.67
        self.module_53 = py_nndct.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[extras]/ModuleList[3]/2497
        self.module_54 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/input.69
        self.module_55 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[extras]/ModuleList[4]/2517
        self.module_56 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/input.71
        self.module_57 = py_nndct.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[extras]/ModuleList[5]/2537
        self.module_58 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/input.73
        self.module_59 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[extras]/ModuleList[6]/2557
        self.module_60 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/input.75
        self.module_61 = py_nndct.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[extras]/ModuleList[7]/2577
        self.module_62 = py_nndct.nn.ReLU(inplace=True) #SSD::SSD/input
        self.module_63 = py_nndct.nn.Conv2d(in_channels=512, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[loc]/ModuleList[0]/2597
        self.module_64 = py_nndct.nn.Module('nndct_permute') #SSD::SSD/2603
        self.module_65 = py_nndct.nn.Module('nndct_contiguous') #SSD::SSD/2605
        self.module_66 = py_nndct.nn.Conv2d(in_channels=512, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[conf]/ModuleList[0]/2624
        self.module_67 = py_nndct.nn.Module('nndct_permute') #SSD::SSD/2630
        self.module_68 = py_nndct.nn.Module('nndct_contiguous') #SSD::SSD/2632
        self.module_69 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=24, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[loc]/ModuleList[1]/2651
        self.module_70 = py_nndct.nn.Module('nndct_permute') #SSD::SSD/2657
        self.module_71 = py_nndct.nn.Module('nndct_contiguous') #SSD::SSD/2659
        self.module_72 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=24, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[conf]/ModuleList[1]/2678
        self.module_73 = py_nndct.nn.Module('nndct_permute') #SSD::SSD/2684
        self.module_74 = py_nndct.nn.Module('nndct_contiguous') #SSD::SSD/2686
        self.module_75 = py_nndct.nn.Conv2d(in_channels=512, out_channels=24, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[loc]/ModuleList[2]/2705
        self.module_76 = py_nndct.nn.Module('nndct_permute') #SSD::SSD/2711
        self.module_77 = py_nndct.nn.Module('nndct_contiguous') #SSD::SSD/2713
        self.module_78 = py_nndct.nn.Conv2d(in_channels=512, out_channels=24, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[conf]/ModuleList[2]/2732
        self.module_79 = py_nndct.nn.Module('nndct_permute') #SSD::SSD/2738
        self.module_80 = py_nndct.nn.Module('nndct_contiguous') #SSD::SSD/2740
        self.module_81 = py_nndct.nn.Conv2d(in_channels=256, out_channels=24, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[loc]/ModuleList[3]/2759
        self.module_82 = py_nndct.nn.Module('nndct_permute') #SSD::SSD/2765
        self.module_83 = py_nndct.nn.Module('nndct_contiguous') #SSD::SSD/2767
        self.module_84 = py_nndct.nn.Conv2d(in_channels=256, out_channels=24, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[conf]/ModuleList[3]/2786
        self.module_85 = py_nndct.nn.Module('nndct_permute') #SSD::SSD/2792
        self.module_86 = py_nndct.nn.Module('nndct_contiguous') #SSD::SSD/2794
        self.module_87 = py_nndct.nn.Conv2d(in_channels=256, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[loc]/ModuleList[4]/2813
        self.module_88 = py_nndct.nn.Module('nndct_permute') #SSD::SSD/2819
        self.module_89 = py_nndct.nn.Module('nndct_contiguous') #SSD::SSD/2821
        self.module_90 = py_nndct.nn.Conv2d(in_channels=256, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[conf]/ModuleList[4]/2840
        self.module_91 = py_nndct.nn.Module('nndct_permute') #SSD::SSD/2846
        self.module_92 = py_nndct.nn.Module('nndct_contiguous') #SSD::SSD/2848
        self.module_93 = py_nndct.nn.Conv2d(in_channels=256, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[loc]/ModuleList[5]/2867
        self.module_94 = py_nndct.nn.Module('nndct_permute') #SSD::SSD/2873
        self.module_95 = py_nndct.nn.Module('nndct_contiguous') #SSD::SSD/2875
        self.module_96 = py_nndct.nn.Conv2d(in_channels=256, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #SSD::SSD/Conv2d[conf]/ModuleList[5]/2894
        self.module_97 = py_nndct.nn.Module('nndct_permute') #SSD::SSD/2900
        self.module_98 = py_nndct.nn.Module('nndct_contiguous') #SSD::SSD/2902
        self.module_99 = py_nndct.nn.Module('nndct_shape') #SSD::SSD/2904
        self.module_100 = py_nndct.nn.Module('nndct_reshape') #SSD::SSD/2909
        self.module_101 = py_nndct.nn.Module('nndct_shape') #SSD::SSD/2911
        self.module_102 = py_nndct.nn.Module('nndct_reshape') #SSD::SSD/2916
        self.module_103 = py_nndct.nn.Module('nndct_shape') #SSD::SSD/2918
        self.module_104 = py_nndct.nn.Module('nndct_reshape') #SSD::SSD/2923
        self.module_105 = py_nndct.nn.Module('nndct_shape') #SSD::SSD/2925
        self.module_106 = py_nndct.nn.Module('nndct_reshape') #SSD::SSD/2930
        self.module_107 = py_nndct.nn.Module('nndct_shape') #SSD::SSD/2932
        self.module_108 = py_nndct.nn.Module('nndct_reshape') #SSD::SSD/2937
        self.module_109 = py_nndct.nn.Module('nndct_shape') #SSD::SSD/2939
        self.module_110 = py_nndct.nn.Module('nndct_reshape') #SSD::SSD/2944
        self.module_111 = py_nndct.nn.Cat() #SSD::SSD/2947
        self.module_112 = py_nndct.nn.Module('nndct_shape') #SSD::SSD/2949
        self.module_113 = py_nndct.nn.Module('nndct_reshape') #SSD::SSD/2954
        self.module_114 = py_nndct.nn.Module('nndct_shape') #SSD::SSD/2956
        self.module_115 = py_nndct.nn.Module('nndct_reshape') #SSD::SSD/2961
        self.module_116 = py_nndct.nn.Module('nndct_shape') #SSD::SSD/2963
        self.module_117 = py_nndct.nn.Module('nndct_reshape') #SSD::SSD/2968
        self.module_118 = py_nndct.nn.Module('nndct_shape') #SSD::SSD/2970
        self.module_119 = py_nndct.nn.Module('nndct_reshape') #SSD::SSD/2975
        self.module_120 = py_nndct.nn.Module('nndct_shape') #SSD::SSD/2977
        self.module_121 = py_nndct.nn.Module('nndct_reshape') #SSD::SSD/2982
        self.module_122 = py_nndct.nn.Module('nndct_shape') #SSD::SSD/2984
        self.module_123 = py_nndct.nn.Module('nndct_reshape') #SSD::SSD/2989
        self.module_124 = py_nndct.nn.Cat() #SSD::SSD/2992
        self.module_125 = py_nndct.nn.Module('nndct_shape') #SSD::SSD/2994
        self.module_126 = py_nndct.nn.Module('nndct_reshape') #SSD::SSD/3000
        self.module_127 = py_nndct.nn.Module('nndct_shape') #SSD::SSD/3002
        self.module_128 = py_nndct.nn.Module('nndct_reshape') #SSD::SSD/3008
        self.L2Norm_weight = torch.nn.parameter.Parameter(torch.Tensor(512,))

    @py_nndct.nn.forward_processor
    def forward(self, *args):
        output_module_0 = self.module_0(data=1.000000013351432e-10, dtype=torch.float, device='cpu')
        output_module_1 = self.module_1(input=args[0])
        output_module_1 = self.module_2(output_module_1)
        output_module_1 = self.module_3(output_module_1)
        output_module_1 = self.module_4(output_module_1)
        output_module_1 = self.module_5(output_module_1)
        output_module_1 = self.module_6(output_module_1)
        output_module_1 = self.module_7(output_module_1)
        output_module_1 = self.module_8(output_module_1)
        output_module_1 = self.module_9(output_module_1)
        output_module_1 = self.module_10(output_module_1)
        output_module_1 = self.module_11(output_module_1)
        output_module_1 = self.module_12(output_module_1)
        output_module_1 = self.module_13(output_module_1)
        output_module_1 = self.module_14(output_module_1)
        output_module_1 = self.module_15(output_module_1)
        output_module_1 = self.module_16(output_module_1)
        output_module_1 = self.module_17(output_module_1)
        output_module_1 = self.module_18(output_module_1)
        output_module_1 = self.module_19(output_module_1)
        output_module_1 = self.module_20(output_module_1)
        output_module_1 = self.module_21(output_module_1)
        output_module_1 = self.module_22(output_module_1)
        output_module_1 = self.module_23(output_module_1)
        output_module_1 = self.module_24(output_module_1)
        output_module_25 = self.module_25({'self': output_module_1,'exponent': 2})
        output_module_25 = self.module_26(input=output_module_25, dim=1, keepdim=True)
        output_module_25 = self.module_27({'self': output_module_25})
        output_module_25 = self.module_28(input=output_module_25, other=output_module_0, alpha=1)
        output_module_29 = self.module_29(input=output_module_1, other=output_module_25)
        output_module_30 = self.module_30(input=self.L2Norm_weight, dim=0)
        output_module_31 = self.module_31(input=output_module_30, dim=2)
        output_module_32 = self.module_32(input=output_module_31, dim=3)
        output_module_32 = self.module_33(input=output_module_32, other=output_module_29)
        output_module_32 = self.module_34(input=output_module_32, other=output_module_29)
        output_module_35 = self.module_35(output_module_1)
        output_module_35 = self.module_36(output_module_35)
        output_module_35 = self.module_37(output_module_35)
        output_module_35 = self.module_38(output_module_35)
        output_module_35 = self.module_39(output_module_35)
        output_module_35 = self.module_40(output_module_35)
        output_module_35 = self.module_41(output_module_35)
        output_module_35 = self.module_42(output_module_35)
        output_module_35 = self.module_43(output_module_35)
        output_module_35 = self.module_44(output_module_35)
        output_module_35 = self.module_45(output_module_35)
        output_module_35 = self.module_46(output_module_35)
        output_module_47 = self.module_47(output_module_35)
        output_module_47 = self.module_48(output_module_47)
        output_module_47 = self.module_49(output_module_47)
        output_module_47 = self.module_50(output_module_47)
        output_module_51 = self.module_51(output_module_47)
        output_module_51 = self.module_52(output_module_51)
        output_module_51 = self.module_53(output_module_51)
        output_module_51 = self.module_54(output_module_51)
        output_module_55 = self.module_55(output_module_51)
        output_module_55 = self.module_56(output_module_55)
        output_module_55 = self.module_57(output_module_55)
        output_module_55 = self.module_58(output_module_55)
        output_module_59 = self.module_59(output_module_55)
        output_module_59 = self.module_60(output_module_59)
        output_module_59 = self.module_61(output_module_59)
        output_module_59 = self.module_62(output_module_59)
        output_module_63 = self.module_63(output_module_32)
        output_module_63 = self.module_64(dims=[0,2,3,1], input=output_module_63)
        output_module_63 = self.module_65(output_module_63)
        output_module_66 = self.module_66(output_module_32)
        output_module_66 = self.module_67(dims=[0,2,3,1], input=output_module_66)
        output_module_66 = self.module_68(output_module_66)
        output_module_69 = self.module_69(output_module_35)
        output_module_69 = self.module_70(dims=[0,2,3,1], input=output_module_69)
        output_module_69 = self.module_71(output_module_69)
        output_module_72 = self.module_72(output_module_35)
        output_module_72 = self.module_73(dims=[0,2,3,1], input=output_module_72)
        output_module_72 = self.module_74(output_module_72)
        output_module_75 = self.module_75(output_module_47)
        output_module_75 = self.module_76(dims=[0,2,3,1], input=output_module_75)
        output_module_75 = self.module_77(output_module_75)
        output_module_78 = self.module_78(output_module_47)
        output_module_78 = self.module_79(dims=[0,2,3,1], input=output_module_78)
        output_module_78 = self.module_80(output_module_78)
        output_module_81 = self.module_81(output_module_51)
        output_module_81 = self.module_82(dims=[0,2,3,1], input=output_module_81)
        output_module_81 = self.module_83(output_module_81)
        output_module_84 = self.module_84(output_module_51)
        output_module_84 = self.module_85(dims=[0,2,3,1], input=output_module_84)
        output_module_84 = self.module_86(output_module_84)
        output_module_87 = self.module_87(output_module_55)
        output_module_87 = self.module_88(dims=[0,2,3,1], input=output_module_87)
        output_module_87 = self.module_89(output_module_87)
        output_module_90 = self.module_90(output_module_55)
        output_module_90 = self.module_91(dims=[0,2,3,1], input=output_module_90)
        output_module_90 = self.module_92(output_module_90)
        output_module_93 = self.module_93(output_module_59)
        output_module_93 = self.module_94(dims=[0,2,3,1], input=output_module_93)
        output_module_93 = self.module_95(output_module_93)
        output_module_96 = self.module_96(output_module_59)
        output_module_96 = self.module_97(dims=[0,2,3,1], input=output_module_96)
        output_module_96 = self.module_98(output_module_96)
        output_module_99 = self.module_99(input=output_module_63, dim=0)
        output_module_100 = self.module_100(input=output_module_63, shape=[output_module_99,-1])
        output_module_101 = self.module_101(input=output_module_69, dim=0)
        output_module_102 = self.module_102(input=output_module_69, shape=[output_module_101,-1])
        output_module_103 = self.module_103(input=output_module_75, dim=0)
        output_module_104 = self.module_104(input=output_module_75, shape=[output_module_103,-1])
        output_module_105 = self.module_105(input=output_module_81, dim=0)
        output_module_106 = self.module_106(input=output_module_81, shape=[output_module_105,-1])
        output_module_107 = self.module_107(input=output_module_87, dim=0)
        output_module_108 = self.module_108(input=output_module_87, shape=[output_module_107,-1])
        output_module_109 = self.module_109(input=output_module_93, dim=0)
        output_module_110 = self.module_110(input=output_module_93, shape=[output_module_109,-1])
        output_module_100 = self.module_111(dim=1, tensors=[output_module_100,output_module_102,output_module_104,output_module_106,output_module_108,output_module_110])
        output_module_112 = self.module_112(input=output_module_66, dim=0)
        output_module_113 = self.module_113(input=output_module_66, shape=[output_module_112,-1])
        output_module_114 = self.module_114(input=output_module_72, dim=0)
        output_module_115 = self.module_115(input=output_module_72, shape=[output_module_114,-1])
        output_module_116 = self.module_116(input=output_module_78, dim=0)
        output_module_117 = self.module_117(input=output_module_78, shape=[output_module_116,-1])
        output_module_118 = self.module_118(input=output_module_84, dim=0)
        output_module_119 = self.module_119(input=output_module_84, shape=[output_module_118,-1])
        output_module_120 = self.module_120(input=output_module_90, dim=0)
        output_module_121 = self.module_121(input=output_module_90, shape=[output_module_120,-1])
        output_module_122 = self.module_122(input=output_module_96, dim=0)
        output_module_123 = self.module_123(input=output_module_96, shape=[output_module_122,-1])
        output_module_113 = self.module_124(dim=1, tensors=[output_module_113,output_module_115,output_module_117,output_module_119,output_module_121,output_module_123])
        output_module_125 = self.module_125(input=output_module_100, dim=0)
        output_module_126 = self.module_126(input=output_module_100, shape=[output_module_125,-1,4])
        output_module_127 = self.module_127(input=output_module_113, dim=0)
        output_module_128 = self.module_128(input=output_module_113, shape=[output_module_127,-1,4])
        return (output_module_126,output_module_128)
