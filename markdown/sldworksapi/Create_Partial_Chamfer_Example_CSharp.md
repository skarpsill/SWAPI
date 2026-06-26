---
title: "Add Partial Chamfer Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Partial_Chamfer_Example_CSharp.htm"
---

# Add Partial Chamfer Example (C#)

## Create Partial Chamfer Example (C#)

This example shows how to create a partial chamfer.

```vb
 // ======================================================================
 // Preconditions:
 // 1. Open Public_documents\samples\tutorial\api\Block20.sldprt.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates Chamfer1.
 // 2. Chamfer1 contains two partial chamfers.
 // 3. Inspect the Immediate window.
 //
 // NOTE: Because the model is used elsewhere, do not save changes to it.
 // ======================================================================

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;

 namespace CreatePartialChamfer_CSharp
 {

       partial  class   SolidWorksMacro
      {
            private  ModelDoc2 swModel;
            private  ModelDocExtension swModelDocExt;
            private  FeatureManager swFeatMgr;
            private  SelectionMgr swSelMgr;
            private  Feature swFeat;
            private   SimpleFilletFeatureData2 swFilletData;
            private  PartialEdgeFilletData PartialEdgeAFilletData;
            private  PartialEdgeFilletData PartialEdgeBFilletData;
            private  Edge filletItemA;
            private  Edge filletItemB;
            private  object swFeatDataObj;

            private  bool boolstatus;
            public  void Main()
           {
              swModel = (ModelDoc2)swApp.ActiveDoc;
              swFeatMgr = swModel.FeatureManager;
              swSelMgr = (SelectionMgr)swModel.SelectionManager;

               // Create the fillet feature data object to be a simple fillet type
              swFeatDataObj = swFeatMgr.CreateDefinition((int)swFeatureNameID_e.swFmFillet);
              swFilletData = (SimpleFilletFeatureData2)swFeatDataObj;

               // Initilize the feature type to be a constant radius fillet
              swFilletData.Initialize((int)swSimpleFilletType_e.swConstRadiusFillet);

              // Specialize the feature type to be a chamfer
              swFilletData.ConicTypeForCrossSectionProfile = (int)swFeatureFilletProfileType_e.swFeatureFilletConicRhoZeroChamfer;

              swFilletData.OverflowType = (int)swFilletOverFlowType_e.swFilletOverFlowType_Default;
              swFilletData.DefaultRadius = 0.01;

               // Select two edges to partially chamfer
              boolstatus = swModel.Extension.SelectByRay(-0.0627751435901871, 0.0395396450382464, 0.000603865270420556, 0.156569748366562, -0.551708952719479, -0.81920885333693, 0.0011220164860728, 1,  false, 1, 0);
              boolstatus = swModel.Extension.SelectByRay(0.0644200432014657, 0.039572847309671, 0.0130368065144353, 0.156569748366562, -0.551708952719479, -0.81920885333693, 0.0011220164860728, 1,  true, 1, 0);

              filletItemA = (Edge)swSelMgr.GetSelectedObject6(1, -1);
              filletItemB = (Edge)swSelMgr.GetSelectedObject6(2, -1);
               int errorCode;
              swFilletData.EnablePartialEdgeParameters =   true;
              PartialEdgeAFilletData = (PartialEdgeFilletData)swFilletData.GetPartialEdgeFilletData(filletItemA);
              errorCode = PartialEdgeAFilletData.SetPartialFilletParameters(true, (int)swSimpleFilletPartialEdgeCondition_e.swPartialEdgeDistanceOffset, 0.01,   null,      (int)swSimpleFilletPartialEdgeCondition_e.swPartialEdgeDistanceOffset, 0.03,   null);
              PartialEdgeBFilletData = (PartialEdgeFilletData)swFilletData.GetPartialEdgeFilletData(filletItemB);
               errorCode = PartialEdgeBFilletData.SetPartialFilletParameters(true, (int)swSimpleFilletPartialEdgeCondition_e.swPartialEdgeDistanceOffset, 0.01,  null,  (int)swSimpleFilletPartialEdgeCondition_e.swPartialEdgeDistanceOffset, 0.03,  null);
```

bool warning;

```vb
               swFeat = swFeatMgr.CreateFeature(swFilletData);
            errorCode = swFeat.GetErrorCode2(out warning);
           }

            ///  <summary>
            ///     ''' The SldWorks swApp variable is pre-assigned for you.
            ///     '''  </summary>
            public  SldWorks swApp;
      }

 }
```
