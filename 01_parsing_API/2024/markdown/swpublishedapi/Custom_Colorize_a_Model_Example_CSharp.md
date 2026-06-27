---
title: "Custom Colorize a Model Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swpublishedapi/Custom_Colorize_a_Model_Example_CSharp.htm"
---

# Custom Colorize a Model Example (C#)

This example shows how to colorize a model.

```vb
//----------------------------------------------------------------------------
// Preconditions:
// 1. Create a C# add-in project in Microsoft Visual Studio.
// 2. Copy this sample code to SwAddin.cs of the new project.
// 3. Change the namespace to match the name of your C# project.
// 4. Ensure that PMPHandler.cs is implementing a compatible interface.
// 5. Compile and run the project.
// 6. In SOLIDWORKS open public_documents\samples\tutorial\api\wrench.sldasm.
// 7. Select View > Display > Curvature.
//
// Postconditions:
// 1. The model is colorized as a function of
//    Value = (double)(vertexCoordX + vertexCoordY + vertexCoordZ);
// 2. The Value is displayed and refreshed as the cursor moves over the model.
//
// NOTE: Because the model is used elsewhere,
// do not save changes when closing it.
//----------------------------------------------------------------------------
```

```vb
using System;
 using System.Runtime.InteropServices;
 using System.Collections;
 using System.Reflection;

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swpublished;
 using SolidWorks.Interop.swconst;
 using SOLIDWORKSTools;
 using SOLIDWORKSTools.File;
 using System.Collections.Generic;
 using System.Diagnostics;

 namespace SwCSharpAddin1
 {
     /// <summary>
     /// This add-in custom colorizes document models.
     /// </summary>
     [Guid("918fec9b-55d0-4e7c-bc6a-5eacc88c29d8"), ComVisible(true)]
     [SwAddin(
         Description = "SwColor description",
         Title = "SwColor",
         LoadAtStartup = true
         )]
     public class SwAddin : ISwAddin
     {
         #region Local Variables
         ISldWorks iSwApp = null;
         int addinID = 0;

         #region Event Handler Variables
         Hashtable openDocs = new Hashtable();
         Hashtable colorDocs = new Hashtable();
         SolidWorks.Interop.sldworks.SldWorks SwEventPtr = null;
         #endregion

         // Public Properties
         public ISldWorks SwApp
         {
             get { return iSwApp; }
         }

         public Hashtable OpenDocs
         {
             get { return openDocs; }
         }

         #endregion

         #region SOLIDWORKS Registration
         [ComRegisterFunctionAttribute]
         public static void RegisterFunction(Type t)
         {
             #region Get Custom Attribute: SwAddinAttribute
             SwAddinAttribute SWattr = null;
             Type type = typeof(SwAddin);

             foreach (System.Attribute attr in type.GetCustomAttributes(false))
             {
                 if (attr is SwAddinAttribute)
                 {
                     SWattr = attr as SwAddinAttribute;
                     break;
                 }
             }

             #endregion

             try
             {
                 Microsoft.Win32.RegistryKey hklm = Microsoft.Win32.Registry.LocalMachine;
                 Microsoft.Win32.RegistryKey hkcu = Microsoft.Win32.Registry.CurrentUser;

                 string keyname = "SOFTWARE\\SOLIDWORKS\\Addins\\{" + t.GUID.ToString() + "}";
                 Microsoft.Win32.RegistryKey addinkey = hklm.CreateSubKey(keyname);
                 addinkey.SetValue(null, 0);

                 addinkey.SetValue("Description", SWattr.Description);
                 addinkey.SetValue("Title", SWattr.Title);

                 keyname = "Software\\SOLIDWORKS\\AddInsStartup\\{" + t.GUID.ToString() + "}";
                 addinkey = hkcu.CreateSubKey(keyname);
                 addinkey.SetValue(null, Convert.ToInt32(SWattr.LoadAtStartup), Microsoft.Win32.RegistryValueKind.DWord);
             }
             catch (System.NullReferenceException nl)
             {
                 Console.WriteLine("There was a problem registering this dll: SWattr is null. \n\"" + nl.Message + "\"");
                 System.Windows.Forms.MessageBox.Show("There was a problem registering this dll: SWattr is null.\n\"" + nl.Message + "\"");
             }

             catch (System.Exception e)
             {
                 Console.WriteLine(e.Message);

                 System.Windows.Forms.MessageBox.Show("There was a problem registering the function: \n\"" + e.Message + "\"");
             }
         }

         [ComUnregisterFunctionAttribute]
         public static void UnregisterFunction(Type t)
         {
             try
             {
                 Microsoft.Win32.RegistryKey hklm = Microsoft.Win32.Registry.LocalMachine;
                 Microsoft.Win32.RegistryKey hkcu = Microsoft.Win32.Registry.CurrentUser;

                 string keyname = "SOFTWARE\\SOLIDWORKS\\Addins\\{" + t.GUID.ToString() + "}";
                 hklm.DeleteSubKey(keyname);

                 keyname = "Software\\SOLIDWORKS\\AddInsStartup\\{" + t.GUID.ToString() + "}";
                 hkcu.DeleteSubKey(keyname);
             }
             catch (System.NullReferenceException nl)
             {
                 Console.WriteLine("There was a problem unregistering this dll: " + nl.Message);
                 System.Windows.Forms.MessageBox.Show("There was a problem unregistering this dll: \n\"" + nl.Message + "\"");
             }
             catch (System.Exception e)
             {
                 Console.WriteLine("There was a problem unregistering this dll: " + e.Message);
                 System.Windows.Forms.MessageBox.Show("There was a problem unregistering this dll: \n\"" + e.Message + "\"");
             }
         }

         #endregion

         #region ISwAddin Implementation
         public SwAddin()
         {
         }

         public bool ConnectToSW(object ThisSW, int cookie)
         {
             iSwApp = (ISldWorks)ThisSW;
             addinID = cookie;

             //Setup callbacks
             iSwApp.SetAddinCallbackInfo(0,  this, addinID);

             #region Setup the Event Handlers
             SwEventPtr = (SolidWorks.Interop.sldworks.SldWorks)iSwApp;
             AttachEventHandlers();
             #endregion

             return true;
         }

         public bool DisconnectFromSW()
         {
             DetachEventHandlers();

             colorDocs.Clear();

             System.Runtime.InteropServices.Marshal.ReleaseComObject(iSwApp);
             iSwApp = null;
             //The addin _must_ call GC.Collect() here in order to retrieve all managed code pointers
             GC.Collect();
             GC.WaitForPendingFinalizers();

             return true;
         }
         #endregion

         #region Event Methods
         public bool AttachEventHandlers()
         {
             AttachSwEvents();
             //Listen for events on all currently open docs
             AttachEventsToAllDocuments();
             return true;
         }

         private bool AttachSwEvents()
         {
             try
             {
                 SwEventPtr.ActiveDocChangeNotify +=  new   DSldWorksEvents_ActiveDocChangeNotifyEventHandler(OnDocChange);
                 SwEventPtr.DocumentLoadNotify2 +=  new  DSldWorksEvents_DocumentLoadNotify2EventHandler(OnDocLoad);
                 SwEventPtr.FileNewNotify2 +=  new  DSldWorksEvents_FileNewNotify2EventHandler(OnFileNew);
                 SwEventPtr.ActiveModelDocChangeNotify +=  new   DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(OnModelChange);
                 SwEventPtr.FileOpenPostNotify +=  new  DSldWorksEvents_FileOpenPostNotifyEventHandler(FileOpenPostNotify);
                 return true;
             }
             catch (Exception e)
             {
                 Console.WriteLine(e.Message);
                 return false;
             }
         }

         private bool DetachSwEvents()
         {
             try
             {
                 SwEventPtr.ActiveDocChangeNotify -=  new   DSldWorksEvents_ActiveDocChangeNotifyEventHandler(OnDocChange);
                 SwEventPtr.DocumentLoadNotify2 -=  new  DSldWorksEvents_DocumentLoadNotify2EventHandler(OnDocLoad);
                 SwEventPtr.FileNewNotify2 -=  new  DSldWorksEvents_FileNewNotify2EventHandler(OnFileNew);
                 SwEventPtr.ActiveModelDocChangeNotify -=  new   DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(OnModelChange);
                 SwEventPtr.FileOpenPostNotify -=  new  DSldWorksEvents_FileOpenPostNotifyEventHandler(FileOpenPostNotify);
                 return true;
             }
             catch (Exception e)
             {
                 Console.WriteLine(e.Message);
                 return false;
             }

         }

         public void AttachEventsToAllDocuments()
         {
             ModelDoc2 modDoc = (ModelDoc2)iSwApp.GetFirstDocument();
             while (modDoc != null)
             {
                 if (!openDocs.Contains(modDoc))
                 {
                     AttachModelDocEventHandler(modDoc);
                 }
                 modDoc = (ModelDoc2)modDoc.GetNext();
             }
         }

         public bool AttachModelDocEventHandler(ModelDoc2 modDoc)
         {
             if (modDoc == null)
                 return false;

             if (!openDocs.Contains(modDoc))
             {
                 ModelDocExtension modExt = modDoc.Extension;

                 ColorContour colorInt = new ColorContour();
                 modExt.InstallModelColorizer(colorInt);
                 colorDocs.Add(modDoc, colorInt);

                 DocumentEventHandler docHandler = null;

                 switch (modDoc.GetType())
                 {
                     case (int)swDocumentTypes_e.swDocPART:
                         {
                             docHandler = new PartEventHandler(modDoc, this);
                             break;
                         }
                     case (int)swDocumentTypes_e.swDocASSEMBLY:
                         {
                             docHandler = new AssemblyEventHandler(modDoc, this);
                             break;
                         }
                     case (int)swDocumentTypes_e.swDocDRAWING:
                         {
                             docHandler = new DrawingEventHandler(modDoc, this);
                             break;
                         }
                     default:
                         {
                             return false; //Unsupported document type
                         }
                 }
                 docHandler.AttachEventHandlers();
                 openDocs.Add(modDoc, docHandler);
             }
             return true;
         }

         public bool DetachModelEventHandler(ModelDoc2 modDoc)
         {
             DocumentEventHandler docHandler;
             docHandler = (DocumentEventHandler)openDocs[modDoc];

             ModelDocExtension modExt = modDoc.Extension;
             modExt.RemoveModelColorizer(colorDocs[modDoc]);

             colorDocs.Remove(modDoc);
             openDocs.Remove(modDoc);
             modDoc = null;
             docHandler = null;
             modExt = null;

             return true;
         }

         public bool DetachEventHandlers()
         {
             DetachSwEvents();

             //Close events on all currently open docs
             DocumentEventHandler docHandler;
             int numKeys = openDocs.Count;
             object[] keys = new Object[numKeys];

             //Remove all document event handlers
             openDocs.Keys.CopyTo(keys, 0);
             foreach (ModelDoc2 key in keys)
             {
                 docHandler = (DocumentEventHandler)openDocs[key];
                 docHandler.DetachEventHandlers();  //This also removes the pair from the hash
                 docHandler = null;
             }
             return true;
         }
         #endregion

         #region Event Handlers
         //Events
         public int OnDocChange()
         {
             return 0;
         }

         public int OnDocLoad(string docTitle, string docPath)
         {
             return 0;
         }

         int FileOpenPostNotify(string FileName)
         {
             AttachEventsToAllDocuments();
             return 0;
         }

         public int OnFileNew(object newDoc, int docType, string templateName)
         {
             AttachEventsToAllDocuments();
             return 0;
         }

         public int OnModelChange()
         {
             return 0;
         }

         #endregion
     }

     public class ColorContour : ISwColorContour1
     {

         #region ISwColorContour Members

         public int  Color(double Value)
         {
             // Assign colors to Value ranges
             if ((Value > 0.0) & (Value <= 0.025))
                 return System.Drawing.ColorTranslator.ToWin32(System.Drawing.Color.Coral);
             else if ((Value > 0.025) & (Value <= 0.05))
                 return System.Drawing.ColorTranslator.ToWin32(System.Drawing.Color.Salmon);
             else if (Value > 0.05)
                 return System.Drawing.ColorTranslator.ToWin32(System.Drawing.Color.Pink);
             else
                 return System.Drawing.ColorTranslator.ToWin32(System.Drawing.Color.Red);

         }

         public string  DisplayString(double Value)
         {
             // Return what is displayed in the view for the given Value
             return "Value is: " + Value.ToString();
         }

         public bool  NeedsUpdate()
         {
             // Return whether SOLIDWORKS needs to refresh the view
             return true;
         }

         public int  Value(object face, float vertexCoordX, float vertexCoordY, float vertexCoordZ, float normalCoordsX, float normalCoordsY, float normalCoordsZ, out double Value)
         {
             // Define a Value for the selected coordinates
             Value = (double)(vertexCoordX + vertexCoordY + vertexCoordZ);

             return 0;

         }

         #endregion
     }
 }
```
