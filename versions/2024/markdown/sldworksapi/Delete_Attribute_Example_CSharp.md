---
title: "Delete Attribute Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Attribute_Example_CSharp.htm"
---

# Delete Attribute Example (C#)

This example shows how to delete the selected attribute.

```
//-------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Selects Cut-Extrude3.
// 3. Adds attribute att 1 to the selected feature.
// 4. Rebuilds the part.
// 5. Deletes attribute att 1.
// 6. Expand Cut-Extrude3 in the FeatureManager design tree
//    and examine the Immediate window to verify step 5.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace DeleteAttributeCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            //1 = invisible
            //0 = visible
            const int CreateVisible = 0;
            const string AttDefName = "XML_string";
            const string AttLenDimName = "att_name";
            const string AttLenValueName = "att_value";
            const string AttRootName = "att";
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Feature swFeat = null;
            Entity swEnt = default(Entity);
            AttributeDef swAttDef = default(AttributeDef);
            SolidWorks.Interop.sldworks.Attribute swAtt = null;
            Parameter swParamName = default(Parameter);
            Parameter swParamValue = default(Parameter);
            string AttName = "";
            int i = 0;
            bool bRet = false;
            string fileName = null;
            int errors = 0;
            int warnings = 0;

            //Open part document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\smartcomponents\\bearing.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Select feature
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            bRet = swModelDocExt.SelectByID2("Cut-Extrude3", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swEnt = (Entity)swFeat;

            //Set attribute att 1
            swAttDef = (AttributeDef)swApp.DefineAttribute(AttDefName);
            bRet = swAttDef.AddParameter(AttLenDimName, (int)swParamType_e.swParamTypeString, 0.0, 0);
            bRet = swAttDef.AddParameter(AttLenValueName, (int)swParamType_e.swParamTypeDouble, 0.0, 0);
            bRet = swAttDef.Register();
            while (swAtt == null)
            {
                // Get a unique attribute name
                i = i + 1;
                AttName = AttRootName + " " + i.ToString();
                swAtt = (SolidWorks.Interop.sldworks.Attribute)swAttDef.CreateInstance5(swModel, swEnt, AttName, CreateVisible, (int)swInConfigurationOpts_e.swThisConfiguration);
            }
            swParamName = (Parameter)swAtt.GetParameter(AttLenDimName);
            swParamValue = (Parameter)swAtt.GetParameter(AttLenValueName);
            bRet = swParamName.SetStringValue2(AttName + " - " + AttLenDimName, (int)swInConfigurationOpts_e.swAllConfiguration, "");
            bRet = swParamValue.SetDoubleValue2(i * 10, (int)swInConfigurationOpts_e.swAllConfiguration, "");
            if ((swAtt != null))
            {
                Debug.Print("Attribute " + AttName + " created.");
            }
            else
            {
                Debug.Print("Attribute " + AttName + " not created.");
            }

            swModel.ForceRebuild3(true);

            //Delete attribute att 1
            bRet = swModelDocExt.SelectByID2("att 1", "ATTRIBUTE", 0, 0, 0, false, 0, null, 0);
            swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swAtt = (SolidWorks.Interop.sldworks.Attribute)swFeat.GetSpecificFeature2();
            AttName = swAtt.GetName();
            bRet = swAtt.Delete(true);
            if (bRet)
            {
                Debug.Print("Attribute " + AttName + " deleted.");
            }
            else
            {
                Debug.Print("Attritute " + AttName + " not deleted.");
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
