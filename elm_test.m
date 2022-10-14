function [nn, dtw_r] = elm_test(X,Y,nn)
ndata        = size(X, 2);
tempH        = nn.W*X + repmat(nn.b,1,ndata);
switch lower(nn.activefunction)
    case{'s','sig','sigmoid'}
        H = 1 ./ (1 + exp(-tempH));
    case{'t','tanh'}
        H = tanh(tempH);
end
Y_hat    = nn.beta*H;
clear H;
dtw_r = [];
if ismember(nn.type,{'c','classification','Classification'})
    [~,label_actual]  = max(Y_hat,[],1);
    if ~isempty(Y)
        [~,label_desired] = max(Y,[],1);
        dtw_r = sum(label_actual==label_desired)/ndata;
    end
else
    if ~isempty(Y)
        dtw_r = dtw(Y_hat,Y); 
        nn.testlabel  = Y_hat;
    else
        nn.testlabel  = Y_hat;
    end
end
