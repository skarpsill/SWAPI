---
title: "Get Model Pathnames from a BOM Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Model_Path_Names_in_BOM_Table_Example_CSharp.htm"
---

# Get Model Pathnames from a BOM Table Example (C#)

This example shows how to get the model pathnames from a specified row of a BOM table annotation.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a drawing containing one BOM table annotation named Bill of Materials1.
 // 2. Modify the namespace to match the name of your C# project.
 // 3. Open an Immediate Window.
 //
 // Postconditions: Inspect the Immediate Window for model pathnames.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 namespace ModelPathNames_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             DrawingDoc swDraw = default(DrawingDoc);
             Feature swFeat = default(Feature);
             BomFeature swBomFeat = default(BomFeature);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swDraw = (DrawingDoc)swModel;
             swFeat = (Feature)swModel.FirstFeature();
             while ((swFeat != null))
             {
                 if ((swFeat.GetTypeName() == "BomFeat"))
                 {
                     Debug.Print("******************************");
                     Debug.Print("Feature Name = " + swFeat.Name);
                     swBomFeat = (BomFeature)swFeat.GetSpecificFeature2();
                     if ((swFeat.Name == "Bill of Materials1"))
                     {
                         ProcessBomFeature(swApp, swModel, swBomFeat);
                     }
                 }
                 swFeat = (Feature)swFeat.GetNextFeature();
             }
         }
         public void ProcessBomFeature(SldWorks swApp, ModelDoc2 swModel, BomFeature swBomFeat)
         {
             GetPathNames(swApp, swBomFeat);
         }

         public void GetPathNames(SldWorks swApp, BomFeature swBomFeature)
         {
             String[] vConfigurations = null;
             string strConfiguration = null;
             Object vVisibility = null;
             int lIdx = 0;
             int lNumConfigurations = 0;
             int lNumRow = 0;
             int lNumColumn = 0;
             int lRow = 0;
             Object[] swBOMTableAnnotationArray = null;
             BomTableAnnotation swBOMTableAnnotation = default(BomTableAnnotation);
             TableAnnotation swTableAnnotation = default(TableAnnotation);
             ModelDoc2 swDocument = default(ModelDoc2);
             AssemblyDoc swAssembly = default(AssemblyDoc);
             string strDocumentName = null;
             int lStartRow = 0;
             bool bGetVisible = false;
             String[] vModelPathNames = null;
             string strItemNumber = "";
             string strPartNumber = "";
             object vModelPathName = null;
             string strModelPathName = null;

             strDocumentName = swBomFeature.GetReferencedModelName();
             swDocument = (ModelDoc2)swApp.GetOpenDocumentByName(strDocumentName);
             Debug.Print("Referenced model = " + strDocumentName);
             swAssembly = (AssemblyDoc)swDocument;

             swBOMTableAnnotationArray = (Object[])swBomFeature.GetTableAnnotations();
             // Get the only BOM table annotation
             swBOMTableAnnotation = (BomTableAnnotation)swBOMTableAnnotationArray[0];
             swTableAnnotation = (TableAnnotation)swBOMTableAnnotation;
             lNumRow = swTableAnnotation.RowCount;
             lNumColumn = swTableAnnotation.ColumnCount;

             lStartRow = 1;

             if ((!(swTableAnnotation.TitleVisible == false)))
             {
                 lStartRow = 2;
             }

             bGetVisible = false;
             Debug.Print("# configurations = " + swBomFeature.GetConfigurationCount(bGetVisible));
             vConfigurations = (String[])swBomFeature.GetConfigurations(bGetVisible, ref vVisibility);

             if (((vConfigurations != null)))
             {
                 lNumConfigurations = vConfigurations.GetUpperBound(0) - vConfigurations.GetLowerBound(0) + 1;
                 for (lIdx = 0; lIdx <= (lNumConfigurations - 1); lIdx++)
                 {
                     strConfiguration = vConfigurations[lIdx];
                     Debug.Print("");
                     Debug.Print("Configuration: " + strConfiguration);

                     for (lRow = lStartRow; lRow <= (lNumRow - 1); lRow++)
                     {
                         Debug.Print("  row = " + (lRow - lStartRow + 1));
                         vModelPathNames = (String[])swBOMTableAnnotation.GetModelPathNames(lRow, out strItemNumber, out strPartNumber);

                         Debug.Print("    item number = " + strItemNumber);
                         Debug.Print("    part number = " + strPartNumber);

                         if (((vModelPathNames != null)))
                         {
                             Debug.Print("    # models contributing to row = " + swBOMTableAnnotation.GetModelPathNamesCount(lRow));
                             foreach (String vModelPathName_loopVariable in vModelPathNames)
                             {
                                 vModelPathName = vModelPathName_loopVariable;
                                 strModelPathName = (String)vModelPathName;
                                 Debug.Print("       " + strModelPathName);
                             }
                         }
                         else
                         {
                             Debug.Print("    # models contributing to row = 0");
                             Debug.Assert(false);
                         }
                     }
                 }
             }
         }

         public SldWorks swApp;

     }
 }
```
