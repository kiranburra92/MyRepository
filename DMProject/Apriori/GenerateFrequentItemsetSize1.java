import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class GenerateFrequentItemsetSize1 {
	
	static List<Integer> GenerateFrequent_1_Itemset(Set<String> candidateItemsetSize1) {
		
		/*** Support Count of Candidate 1-Itemset ***/    
	    
		int count[] = new int[candidateItemsetSize1.size()];
	    for(int outer = 0; outer < FrequentK_MiningDriver.transactionAfterIntegerMap.size(); outer++){
	    	Iterator<Integer> c1 = FrequentK_MiningDriver.transactionAfterIntegerMap.get(outer).iterator();
	    	while(c1.hasNext()){
	    		Integer temp = c1.next();
	    		count[temp]++;
	    	}
	    }

	    /*** Frequent 1-Itemset Generation ***/
	    
	    List<Integer> frequentItemsetSize1= new ArrayList<Integer>();
	    List<Integer> frequentItemsetSupportCount = new ArrayList<Integer>();		// NO need of this after this work.
	    for(int i = 0; i < candidateItemsetSize1.size(); i++){
	    	if(count[i] >= FrequentK_MiningDriver.minSupport ){
	    		frequentItemsetSize1.add(i);
	    		frequentItemsetSupportCount.add(count[i]);
	    	}
	    }
	
	    if(FrequentK_MiningDriver.inputKValue == 1 && frequentItemsetSize1.size() > 0){
	    	try{
			    PrintWriter writer = new PrintWriter(FrequentK_MiningDriver.outputFileName, "UTF-8");
			    
			    ArrayList<String> frequentReviewIDs = new ArrayList<String>();
			    
			    for(int k = 0; k < frequentItemsetSize1.size(); k++){
			    	
			    	int temp = frequentItemsetSize1.get(k);
			    	
			    	for(Map.Entry<String,Integer> entry: ReviewerID_StringToIntConversion.uniqueReviewerIDs_Integer.entrySet()){
				    	if(temp == entry.getValue()){
				    		frequentReviewIDs.add(entry.getKey());  
				    		break;
				    	}
				    }
			    }
			    for(int f = 0; f < frequentReviewIDs.size(); f++){
					if(frequentItemsetSupportCount.size() != 0){
						writer.print(frequentReviewIDs.get(f) + " ");
						writer.println("(" + frequentItemsetSupportCount.get(f) + ")");
					}	
				}
				
			    writer.close();
			} catch (IOException e) {
			   System.out.println(e.getMessage());
			}
	    }
		return frequentItemsetSize1;
	}
}
