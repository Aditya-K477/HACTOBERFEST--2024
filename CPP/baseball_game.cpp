class Solution {
public:
    int calPoints(vector<string>& operations) {

        int n = operations.size();

        vector<int> record;
        // storing the scores of the baseball means!!

        for(int i = 0; i < n; i++){

            if(operations[i] != "D" && operations[i] != "C" && operations[i] != "+"){
            // stoi() function is used in order to convert a string into an array 
                record.push_back(stoi(operations[i]));
            }
            else if(operations[i] == "+"){
            // here we need to use record.size() and not the index just because there might be a condition where the size of the array is lesser than 
            // the index we are at, in that case it might throw an error
                record.push_back(record[record.size()-1] + record[record.size()-2]);
            }
            else if(operations[i] == "C"){
            
                record.pop_back();
            }
            else if(operations[i] == "D"){

                record.push_back(2 * record[record.size()-1]);
            }
        }

        int sum = 0;
        // to store the sum of all the records during the basketball game

        for(int i = 0; i < record.size(); i++){
         
            sum += record[i];

        }
        return sum;
        
    }
};