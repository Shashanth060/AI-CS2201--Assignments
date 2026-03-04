#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*  We are using structure that stores one AQI breakpoint range.
    For each pollutant range (BP_lo to BP_hi),
    there is a AQI index range (I_lo to I_hi) as given in pdf*/

typedef struct
{
    float BP_lo, BP_hi;
    int I_lo, I_hi;
} AQIRange;

/*  Breakpoint tables
    Source: [UrbanEmissions SIM-46-2021 AQI Guidelines](https://urbanemissions.info/wp-content/uploads/docs/SIM-46-2021.pdf)*/

//All the Ranges are reffered from UrbanEmissions SIM-46-2021 AQI Guidelines
/* PM2.5 */
AQIRange pm25_bp[] = {
    {0, 30, 0, 50},
    {30, 60, 51, 100},
    {60, 90, 101, 200},
    {90, 120, 201, 300},
    {120, 250, 301, 400},
    {250, 1000, 401, 500}};

/* PM10 */
AQIRange pm10_bp[] = {
    {0, 50, 0, 50},
    {50, 100, 51, 100},
    {100, 250, 101, 200},
    {250, 350, 201, 300},
    {350, 430, 301, 400},
    {430, 1000, 401, 500}};

/* NO2 */
AQIRange no2_bp[] = {
    {0, 40, 0, 50},
    {40, 80, 51, 100},
    {80, 180, 101, 200},
    {180, 280, 201, 300},
    {280, 400, 301, 400},
    {400, 1000, 401, 500}};

/* SO2 */
AQIRange so2_bp[] = {
    {0, 40, 0, 50},
    {40, 80, 51, 100},
    {80, 380, 101, 200},
    {380, 800, 201, 300},
    {800, 1600, 301, 400},
    {1600, 2000, 401, 500}};

/* CO (mg/m3) */
AQIRange co_bp[] = {
    {0, 1, 0, 50},
    {1, 2, 51, 100},
    {2, 10, 101, 200},
    {10, 17, 201, 300},
    {17, 34, 301, 400},
    {34, 50, 401, 500}};

/* O3 */
AQIRange o3_bp[] = {
    {0, 50, 0, 50},
    {50, 100, 51, 100},
    {100, 168, 101, 200},
    {168, 208, 201, 300},
    {208, 748, 301, 400},
    {748, 1000, 401, 500}};


//Calculation of AQI sub-index for a pollutant concentration
float calculate_subAQI(float C, AQIRange bp[], int size)
{
    for (int i = 0; i < size; i++)
    {
        if (C >= bp[i].BP_lo && C <= bp[i].BP_hi)
        {
            return ((float)(bp[i].I_hi - bp[i].I_lo) /
                    (bp[i].BP_hi - bp[i].BP_lo)) *
                       (C - bp[i].BP_lo) +
                   bp[i].I_lo;
        }
    }

    if (C > bp[size - 1].BP_hi)
        return 500;

    return 0;
}

/* AQI Category */
const char *category(int AQI)
{
    if (AQI <= 50)
        return "Good";
    else if (AQI <= 100)
        return "Satisfactory";
    else if (AQI <= 200)
        return "Moderate";
    else if (AQI <= 300)
        return "Poor";
    else if (AQI <= 400)
        return "Very Poor";
    else
        return "Severe";
}


void read_data(const char *filename,
               float *pm25, float *pm10,
               float *no2, float *so2,
               float *co, float *o3)
{
    FILE *f = fopen(filename, "r");
    if (!f)
    {
        printf("Error in opening the file\n");
        exit(1);
    }

    char line[100], key[20];
    float value;

    while (fgets(line, sizeof(line), f))
    {
        sscanf(line, "%[^=]=%f", key, &value);

        if (strcmp(key, "PM25") == 0)
            *pm25 = value;
        else if (strcmp(key, "PM10") == 0)
            *pm10 = value;
        else if (strcmp(key, "NO2") == 0)
            *no2 = value;
        else if (strcmp(key, "SO2") == 0)
            *so2 = value;
        else if (strcmp(key, "CO") == 0)
            *co = value;
        else if (strcmp(key, "O3") == 0)
            *o3 = value;
    }

    fclose(f);
}

int main()
{
    float PM25 = 0, PM10 = 0, NO2 = 0, SO2 = 0, CO = 0, O3 = 0;

    read_data("data.txt", &PM25, &PM10, &NO2, &SO2, &CO, &O3);

    float aqi_pm25 = calculate_subAQI(PM25, pm25_bp, 6);
    float aqi_pm10 = calculate_subAQI(PM10, pm10_bp, 6);
    float aqi_no2 = calculate_subAQI(NO2, no2_bp, 6);
    float aqi_so2 = calculate_subAQI(SO2, so2_bp, 6);
    float aqi_co = calculate_subAQI(CO, co_bp, 6);
    float aqi_o3 = calculate_subAQI(O3, o3_bp, 6);

    /* We choose AQI with worst pollutant */
    float AQI = aqi_pm25;

    if (aqi_pm10 > AQI)
        AQI = aqi_pm10;
    if (aqi_no2 > AQI)
        AQI = aqi_no2;
    if (aqi_so2 > AQI)
        AQI = aqi_so2;
    if (aqi_co > AQI)
        AQI = aqi_co;
    if (aqi_o3 > AQI)
        AQI = aqi_o3;

    printf("Final AQI: %d\n", (int)AQI);
    printf("Category: %s\n", category((int)AQI));

    return 0;
}