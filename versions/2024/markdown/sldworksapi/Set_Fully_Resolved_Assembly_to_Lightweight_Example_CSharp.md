---
title: "Set Fully Resolved Assembly to Lightweight Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Fully_Resolved_Assembly_to_Lightweight_Example_CSharp.htm"
---

# Set Fully Resolved Assembly to Lightweight Example (C#)

This example shows how to set a fully resolved assembly to lightweight.

```
//----------------------------------------------------------------
// Preconditions:
// 1. Open a fully resolved assembly document.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Sets all assembly components to lightweight.
// 2. Examine the Immediate window and FeatureManager design tree.
//----------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace SetSuppression2.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            AssemblyDoc swAssy = default(AssemblyDoc);
            Configuration swConfig = default(Configuration);
            ConfigurationManager swConfigMgr = default(ConfigurationManager);
            Component2 swRootComp = default(Component2);
            bool bRet = false;
            string sPadStr = "  ";

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssy = (AssemblyDoc)swModel;
            swConfigMgr = (ConfigurationManager)swModel.ConfigurationManager;
            swConfig = (Configuration)swConfigMgr.ActiveConfiguration;
            swRootComp = (Component2)swConfig.GetRootComponent3(true);
            Debug.Print("File = " + swModel.GetPathName());
            SetComponentLightWeight(sPadStr, swRootComp);

            // Update in-context features
            bRet = swModel.ForceRebuild3(false);
            Debug.Assert(bRet);

        }

        public void SetComponentLightWeight(string sPadStr, Component2 swComp)
        {
            object[] vChildArr = null;
            Component2 swChildComp = default(Component2);
            ModelDoc2 swChildModel = default(ModelDoc2);
            int nRetVal = 0;
            int nDocType = 0;
            int i = 0;

            Debug.Print(sPadStr + swComp.Name2 + " [" + Convert.ToBoolean(swComp.Visible) + "]");
            vChildArr = (object[])swComp.GetChildren();
            for (i = 0; i < vChildArr.Length; i++)
            {
                swChildComp = (Component2)vChildArr[i];
                // Is null if another instance has been previously set to lightweight
                swChildModel = (ModelDoc2)swChildComp.GetModelDoc2();
                if ((swChildModel != null))
                {
                    nDocType = swChildModel.GetType();
                }
                else
                {
                    nDocType = (int)swDocumentTypes_e.swDocNONE;
                }
                nRetVal = swChildComp.SetSuppression2((int)swComponentSuppressionState_e.swComponentLightweight);
                if ((int)swDocumentTypes_e.swDocPART == nDocType | (int)swDocumentTypes_e.swDocNONE == nDocType)
                {
                    Debug.Assert((int)swComponentResolveStatus_e.swResolveNotPerformed == nRetVal);
                }
                else
                {
                    // Cannot set a sub-assembly to lightweight; must set each part to lightweight
                    Debug.Assert((int)swDocumentTypes_e.swDocASSEMBLY == swChildModel.GetType());
                    Debug.Assert((int)swComponentResolveStatus_e.swResolveError == nRetVal);
                }
                // Recurse into this component
                SetComponentLightWeight(sPadStr + "  ", swChildComp);

            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
