---
title: "Get Mate Reference Properties Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mate_Reference_Properties_Example_CSharp.htm"
---

# Get Mate Reference Properties Example (C#)

This example shows how to get mate reference properties.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the part.
// 2. Inserts a mate reference.
// 3. Gets properties of mate reference.
// 4. Examine the FeatureManager design tree and Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
// ---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {

        public void Main()
        {
            MateReference swMateReference = default(MateReference);
            Feature swFeature = default(Feature);
            object mateRefObj = null;
            int mateRefEntityType = 0;
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Entity swPlane = default(Entity);
            FeatureManager swFeatureMgr = default(FeatureManager);
            string strMateReferencename = null;
            int nCount = 0;
            int refEntType = 0;
            int mateRefAlignment = 0;
            bool boolstatus = false;
            string fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\fillets\\knob.sldprt";
            int errors = 0;
            int warnings = 0;

            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Insert mate reference
            boolstatus = swModelDocExt.SelectByID2("Front", "PLANE", 0, 0, 0, true, 1, null, 0);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swPlane = (Entity)swSelMgr.GetSelectedObject6(1, -1);
            boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.00835786916030656, 0.00429540237419701, 0, true, 2, null, 0);
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureMgr.InsertMateReference2("Default", null, 0, 1, false, null, 0, 2, false, null,
            0, 0);
            swModel.ClearSelection2(true);
            boolstatus = swModelDocExt.SelectByID2("Default-<1>", "POSGROUP", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swMateReference = (MateReference)swFeature.GetSpecificFeature2();
            swModel.ClearSelection2(true);

            // Get the name of the mate reference
            strMateReferencename = swMateReference.Name;
            Debug.Print("Name of mate reference = " + strMateReferencename);

            // Get the number of reference entities in the mate reference
            nCount = swMateReference.ReferenceEntityCount;
            Debug.Print("Number of mate reference entities = " + nCount);

            // Get the mate reference type for the primary mate
            // entity in the selected mate reference
            refEntType = swMateReference.get_ReferenceType(0);
            Debug.Print("Mating type of primary mate entity = " + refEntType);

            // Get the mate reference alignment for the
            // mate reference entity in the selected mate reference
            mateRefAlignment = swMateReference.get_ReferenceAlignment(0);
            Debug.Print("Alignment of primary mate entity = " + mateRefAlignment);

            // Get the  mate reference entity in the mate reference
            mateRefObj = swMateReference.get_ReferenceEntity2(0);

            // Get the mate reference entity type
            mateRefEntityType = swMateReference.get_ReferenceEntityType(0);
            Debug.Print("Entity type of primary mate entity = " + mateRefEntityType);

            // QueryInterface the returned object as a face, if a face

            if (mateRefEntityType == (int)swSelectType_e.swSelFACES)
            {
                Face2 mateRefFace = default(Face2);
                mateRefFace = (Face2)mateRefObj;

                Debug.Print("Primary mate entity is a face with area = " + mateRefFace.GetArea());

            }

            swModel.ClearSelection2(true);

        }

        public SldWorks swApp;

    }
}
```
