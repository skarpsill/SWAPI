---
title: "Get Part's Feature Statistics Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Part's_Feature_Statistics_Example_CSharp.htm"
---

# Get Part's Feature Statistics Example (C#)

This example shows how to get the statistics of all of the features
in a part document.

```
//-------------------------------------------
// Preconditions:
// 1. Open a part that has multiple features.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets the statistics for the features in
//    the part.
// 2. Examine the Immediate window.
//-------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace GetFeatureStatisticsForPart_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial
 class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public
 void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}FeatureStatistics swFeatStat = default(FeatureStatistics);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}FeatureManager swFeatMgr = default(FeatureManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}String[] featnames = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Int32[] feattypes = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Object[]
 features = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Double[] featureUpdateTimes = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Double[] featureUpdatePercentTimes = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int iter = 0;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeatMgr = swModel.FeatureManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeatStat = swFeatMgr.FeatureStatistics;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeatStat.Refresh();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Model name: " + swFeatStat.PartName);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("
 Number of features: " + swFeatStat.FeatureCount);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("
 Number of solid bodies: " + swFeatStat.SolidBodiesCount);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("
 Number of surface bodies: " + swFeatStat.SurfaceBodiesCount);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("
 Total rebuild time: " + swFeatStat.TotalRebuildTime);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}features
 = (Object[])swFeatStat.Features;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}featnames = (String[])swFeatStat.FeatureNames;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}feattypes = (Int32[])swFeatStat.FeatureTypes;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}featureUpdateTimes = (Double[])swFeatStat.FeatureUpdateTimes;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}featureUpdatePercentTimes = (Double[])swFeatStat.FeatureUpdatePercentageTimes;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if
 ((featnames != null))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}for
 (iter = 0; iter <= featnames.GetUpperBound(0); iter++)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("
 Feature name: " + featnames[iter]);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("
 Feature created: " + ((Feature)features[iter]).DateCreated);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("
 Feature type as defined in sw_SelectType_e: " + feattypes[iter]);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("
 Update time: " + featureUpdateTimes[iter]);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("
 Update % time: " + featureUpdatePercentTimes[iter]);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
