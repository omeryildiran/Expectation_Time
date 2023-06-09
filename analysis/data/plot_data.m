
% Set the path to the data files
%path = 'C:/Users/omeru/Documents/Omer_Repos/Internship Pascal/Expectation_Shapes_Perceived_Time_final/analysis/data/';

% Load the data file
data_Erva = 'niho_pilot_base_expectation_shapes_perceived_time_2023-03-16_23h46.19.804.csv';
data_Nicola = 'nicola_base_pilot_expectation_shapes_perceived_time_2023-03-20_15h03.16.305.csv';
data_Omer = '299271_expectation_shapes_perceived_time_2023-03-19_15h42.48.633.csv';
data_Omer2 = 'omer_pilot2_expectation_shapes_perceived_time_2023-03-17_00h51.58.576.csv';

%df = readtable(strcat(path, data_Erva));
df = importdata(data_Omer2);
df=df.textdata;
df=cell2table(df);
% Add additional columns
df.delayS = df.delay/1000;
df.pTemporalError = df.perceivedTime - df.targetstarted;
df.pTemporalErrorMS = df.pTemporalError * 1000;
df.physicalDelay = df.distractorstarted - df.targetstarted;
df.physicalDelayMS = df.physicalDelay * 1000;
df = df(df.isTrial == 'trial', :);
df = df(~isnan(df.pTemporalError), :);

% Group the data by delayS and calculate the means and standard deviations
df_means = groupsummary(df, 'delayS', 'mean');
df_stdDev = groupsummary(df, 'delayS', 'std');
a = unique(df.delay);
a = sort(a);
df_means.delayMs = a;

% Perform curve fitting
xdata = df_means.physicalDelayMS;
ydata = df_means.pTemporalErrorMS;
[parameters, covariance] = curve_fit(@model_time_base, xdata, ydata);
fit_A = parameters(1);
fit_B = parameters(2);
fprintf('fit_A = %f\n', fit_A);
fprintf('fit_B = %f\n', fit_B);
fit_y = model_time_base(xdata, fit_A, fit_B);

% Plot the results
figure('Position', [0 0 1500 1200]);
plot(xdata, ydata, 'o', 'DisplayName', 'data');
hold on;
plot(xdata, fit_y, '-', 'DisplayName', 'fit');
ax = gca;
ax.XAxis.Color = 'black';
ax.YAxis.Color = 'black';
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
ax.XGrid = 'off';
ax.YGrid = 'off';
ax.XLim = [-1000, 1000];
ax.YLim = [-200, 200];
ax.XTick = [-1000:200:1000];
ax.YTick = [-200:50:200];
xlabel('Physical delay (ms)', 'FontSize', 16, 'FontWeight', 'bold');
ylabel('Perceived error (ms)', 'FontSize', 16, 'FontWeight', 'bold');
%title('Model fit to data', 'FontSize', 20, 'Font

% Define the model function
function modelPerceivedError = model_time_base(delay, alpha, sigma)
modelPerceivedError = alpha.*(delay./sigma).*exp(-(delay.^2)./sigma^2);
modelPerceivedError = modelPerceivedError * 1000;
end
