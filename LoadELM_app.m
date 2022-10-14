function LoadELM_app(ELMPATH,RELMPATH)

tabela = readtable('ForELMAndRELM_app.csv');
tabela = rows2vars(tabela);
tabela = removevars(tabela,{'OriginalVariableNames','Var1'});

nn = load(ELMPATH);

[nn1, acc_test]   = elm_test(table2array(tabela(:,1:3))', table2array(tabela(:,4:end))', nn);

fileID = fopen("ResultsELMTeste.csv",'w+');
fprintf(fileID,'F_PRO_1,F_PRO_2,F_PRO_3,F_PRO_4,F_PRO_5,F_PRO_6,F_PRO_7,F_PRO_8,F_PRO_9,F_PRO_10,F_PRO_11,F_PRO_12,F_PRO_13,F_PRO_14,F_PRO_15,F_PRO_16,F_PRO_17,F_PRO_18,F_PRO_19,F_PRO_20,F_PRO_21,F_PRO_22,F_PRO_23,F_PRO_24,F_PRO_25,F_PRO_26,F_PRO_27,F_PRO_28,F_PRO_29,F_PRO_30,F_PRO_31,F_PRO_32,F_PRO_33,F_PRO_34,F_PRO_35,F_PRO_36,F_PRO_37,F_PRO_38,F_PRO_39,F_PRO_40,F_PRO_41,F_PRO_42,F_PRO_43,F_PRO_44,F_PRO_45,F_PRO_46,F_PRO_47,F_PRO_48,F_PRO_49,F_PRO_50,F_PRO_51,F_PRO_52,F_PRO_53,F_PRO_54,F_PRO_55,F_PRO_56,F_PRO_57,F_PRO_58,F_PRO_59,F_PRO_60,F_PRO_61,F_PRO_62,F_PRO_63,F_PRO_64,F_PRO_65,F_PRO_66,F_PRO_67,F_PRO_68,F_PRO_69,F_PRO_70,F_PRO_71,F_PRO_72,F_PRO_73,F_PRO_74,F_PRO_75,F_PRO_76,F_PRO_77,F_PRO_78,F_PRO_79,F_PRO_80,F_PRO_81,F_PRO_82,F_PRO_83,F_PRO_84,F_PRO_85,F_PRO_86,F_PRO_87,F_PRO_88,F_PRO_89,F_PRO_90,F_PRO_91,F_PRO_92,F_PRO_93,F_PRO_94,F_PRO_95,F_PRO_96,F_PRO_97,F_PRO_98,F_PRO_99,F_PRO_100,F_PRO_101\n');
for i=1:length(nn1.testlabel)
    if(i==1)
        fprintf(fileID,'%s',num2str((nn1.testlabel(i,1))));
    else
        fprintf(fileID,',%s',num2str((nn1.testlabel(i,1))));
    end
end
fclose(fileID);

nn = load(RELMPATH);

[nn1, acc_test]   = elm_test(table2array(tabela(:,1:3))', table2array(tabela(:,4:end))', nn);

fileID = fopen("ResultsRELMTeste.csv",'w+');
fprintf(fileID,'F_PRO_1,F_PRO_2,F_PRO_3,F_PRO_4,F_PRO_5,F_PRO_6,F_PRO_7,F_PRO_8,F_PRO_9,F_PRO_10,F_PRO_11,F_PRO_12,F_PRO_13,F_PRO_14,F_PRO_15,F_PRO_16,F_PRO_17,F_PRO_18,F_PRO_19,F_PRO_20,F_PRO_21,F_PRO_22,F_PRO_23,F_PRO_24,F_PRO_25,F_PRO_26,F_PRO_27,F_PRO_28,F_PRO_29,F_PRO_30,F_PRO_31,F_PRO_32,F_PRO_33,F_PRO_34,F_PRO_35,F_PRO_36,F_PRO_37,F_PRO_38,F_PRO_39,F_PRO_40,F_PRO_41,F_PRO_42,F_PRO_43,F_PRO_44,F_PRO_45,F_PRO_46,F_PRO_47,F_PRO_48,F_PRO_49,F_PRO_50,F_PRO_51,F_PRO_52,F_PRO_53,F_PRO_54,F_PRO_55,F_PRO_56,F_PRO_57,F_PRO_58,F_PRO_59,F_PRO_60,F_PRO_61,F_PRO_62,F_PRO_63,F_PRO_64,F_PRO_65,F_PRO_66,F_PRO_67,F_PRO_68,F_PRO_69,F_PRO_70,F_PRO_71,F_PRO_72,F_PRO_73,F_PRO_74,F_PRO_75,F_PRO_76,F_PRO_77,F_PRO_78,F_PRO_79,F_PRO_80,F_PRO_81,F_PRO_82,F_PRO_83,F_PRO_84,F_PRO_85,F_PRO_86,F_PRO_87,F_PRO_88,F_PRO_89,F_PRO_90,F_PRO_91,F_PRO_92,F_PRO_93,F_PRO_94,F_PRO_95,F_PRO_96,F_PRO_97,F_PRO_98,F_PRO_99,F_PRO_100,F_PRO_101\n');
for i=1:length(nn1.testlabel)
    if(i==1)
        fprintf(fileID,'%s',num2str((nn1.testlabel(i,1))));
    else
        fprintf(fileID,',%s',num2str((nn1.testlabel(i,1))));
    end
end
fclose(fileID);


end