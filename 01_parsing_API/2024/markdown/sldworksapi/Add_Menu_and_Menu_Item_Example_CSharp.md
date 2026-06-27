---
title: "Add Menu and Menu Item Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Menu_and_Menu_Item_Example_CSharp.htm"
---

# Add Menu and Menu Item Example (C#)

This example shows how to add a menu and menu item to a part.

```
//---------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the SOLIDWORKS API SDK add-in templates for your version
//    of Microsoft Visual Studio are installed.
// 2. In Microsoft Visual Studio, create a C# project using the
//    SwCSharpAddin template.
// 3. Name the project AddMenuItemCSharp.
// 4. Copy and paste SwAddin into SwAddin.cs of your project.
// 5. Click Project > AddMenuItemCSharp Properties > Debug.
// 6. Select Start external program and type the pathname to your
//    SOLIDWORKS executable.
// 7. Replace the images array elements with the pathnames to
//    your image files.
// 8. Press F5 to start debugging this add-in.
//
// Postconditions:
// 1. In SOLIDWORKS, click File > New > Part > OK.
// 2. Click Tools > MyMenu. Note the size of
//    the MyMenuItem button.
// 3. Click MyMenuItem and click OK to close the message box.
// 4. Exit SOLIDWORKS.
// 5. Change the size of the text and other items on your computer.
//    For example, in Windows 7:
//    a. Click Start > Control Panel > Appearance and
//       Personalization > Display.
//    b. Select a different size.
//    c. Click Apply.
//    d. Click Log off now.
//    e. Log back in.
// 6. Start SOLIDWORKS.
// 7. Repeat steps 1 and 2.
//---------------------------------------------------------------------------
//SwAddin
using System;
using System.Runtime.InteropServices;
using System.Collections;
using System.Reflection;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swpublished;
using SolidWorks.Interop.swconst;
using SolidWorksTools;
using SolidWorksTools.File;
using System.Collections.Generic;
using System.Diagnostics;
using System.Windows.Forms;

namespace AddMenuItemCSharp
{
    /// <summary>
    /// Summary description for AddMenuItemCSharp.
    /// </summary>
    [Guid("ffd413b4-df9a-4d58-b4c2-171c74e72971"), ComVisible(true)]
    [SwAddin(
        Description = "AddMenuItemCSharp description",
        Title = "AddMenuItemCSharp",
        LoadAtStartup = true
        )]
    public class SwAddin : ISwAddin
    {
        #region Local Variables
        ISldWorks iSwApp = null;
        int addinID = 0;

        #region Event Handler Variables
        Hashtable openDocs = new Hashtable();
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

        #region SolidWorks Registration
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

                string keyname = "SOFTWARE\\SolidWorks\\Addins\\{" + t.GUID.ToString() + "}";
                Microsoft.Win32.RegistryKey addinkey = hklm.CreateSubKey(keyname);
                addinkey.SetValue(null, 0);

                addinkey.SetValue("Description", SWattr.Description);
                addinkey.SetValue("Title", SWattr.Title);

                keyname = "Software\\SolidWorks\\AddInsStartup\\{" + t.GUID.ToString() + "}";
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

                string keyname = "SOFTWARE\\SolidWorks\\Addins\\{" + t.GUID.ToString() + "}";
                hklm.DeleteSubKey(keyname);

                keyname = "Software\\SolidWorks\\AddInsStartup\\{" + t.GUID.ToString() + "}";
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

            //Set up callbacks
            iSwApp.SetAddinCallbackInfo2(0, this, addinID);

            #region Setup the menu item
            AddMenuItem();
            #endregion

            #region Set up the Event Handlers
            SwEventPtr = (SolidWorks.Interop.sldworks.SldWorks)iSwApp;
            openDocs = new Hashtable();
            AttachEventHandlers();
            #endregion

            return true;
        }

        public bool DisconnectFromSW()
        {
            DetachEventHandlers();

            System.Runtime.InteropServices.Marshal.ReleaseComObject(iSwApp);
            iSwApp = null;
            // The add-in must call GC.Collect() here to retrieve all managed code pointers
            GC.Collect();
            GC.WaitForPendingFinalizers();

            GC.Collect();
            GC.WaitForPendingFinalizers();

            return true;
        }
        #endregion

        #region UI Methods
        public void AddMenuItem()
        {
	    Assembly thisAssembly = default(Assembly);
            int menuId = 0;
            string[] images = new string[3];

            thisAssembly = System.Reflection.Assembly.GetAssembly(this.GetType());

            images[0] = "K:\\api\\HELP\\Sample Macros\\SW2016\\b2\\ISldWorksAddMenuItem5\\AddMenuItemCSharp\\AddMenuItemCSharp\\Small.bmp";
            images[1] = "K:\\api\\HELP\\Sample Macros\\SW2016\\b2\\ISldWorksAddMenuItem5\\AddMenuItemCSharp\\AddMenuItemCSharp\\Medium.bmp";
            images[2] = "K:\\api\\HELP\\Sample Macros\\SW2016\\b2\\ISldWorksAddMenuItem5\\AddMenuItemCSharp\\AddMenuItemCSharp\\Large.bmp";

	    menuId = SwApp.AddMenu((int)swDocumentTypes_e.swDocPART, "MyMenu", 0);
            menuId = iSwApp.AddMenuItem5((int)swDocumentTypes_e.swDocPART, addinID, "MyMenuItem@MyMenu", 0, "MyMenuCallback", "MyMenuEnableMethod", "My menu item", images);

            thisAssembly = null;

        }
        #endregion

        #region UI Callbacks
        public void MyMenuCallback()
        {
            MessageBox.Show("Callback function called.");
        }
        #endregion

        #region Event Methods
        public bool AttachEventHandlers()
        {
            AttachSwEvents();
            // Listen for events on all currently open docs
            AttachEventsToAllDocuments();
            return true;
        }

        private bool AttachSwEvents()
        {
            try
            {
                SwEventPtr.ActiveDocChangeNotify += new DSldWorksEvents_ActiveDocChangeNotifyEventHandler(ActiveDocChangeNotify);
                SwEventPtr.DocumentLoadNotify2 += new DSldWorksEvents_DocumentLoadNotify2EventHandler(DocumentLoadNotify2);
                SwEventPtr.FileNewNotify2 += new DSldWorksEvents_FileNewNotify2EventHandler(FileNewNotify2);
                SwEventPtr.ActiveModelDocChangeNotify += new DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(ActiveModelDocChangeNotify);
                SwEventPtr.FileOpenPostNotify += new DSldWorksEvents_FileOpenPostNotifyEventHandler(FileOpenPostNotify);
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
                SwEventPtr.ActiveDocChangeNotify -= new DSldWorksEvents_ActiveDocChangeNotifyEventHandler(ActiveDocChangeNotify);
                SwEventPtr.DocumentLoadNotify2 -= new DSldWorksEvents_DocumentLoadNotify2EventHandler(DocumentLoadNotify2);
                SwEventPtr.FileNewNotify2 -= new DSldWorksEvents_FileNewNotify2EventHandler(FileNewNotify2);
                SwEventPtr.ActiveModelDocChangeNotify -= new DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(ActiveModelDocChangeNotify);
                SwEventPtr.FileOpenPostNotify -= new DSldWorksEvents_FileOpenPostNotifyEventHandler(FileOpenPostNotify);
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
                else if (openDocs.Contains(modDoc))
                {
                    bool connected = false;
                    DocumentEventHandler docHandler = (DocumentEventHandler)openDocs[modDoc];
                    if (docHandler != null)
                    {
                        connected = docHandler.ConnectModelViews();
                    }
                }

                modDoc = (ModelDoc2)modDoc.GetNext();
            }
        }

        public bool AttachModelDocEventHandler(ModelDoc2 modDoc)
        {
            if (modDoc == null)
                return false;

            DocumentEventHandler docHandler = null;

            if (!openDocs.Contains(modDoc))
            {
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
                            // Unsupported document type
                            return false;
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
            openDocs.Remove(modDoc);
            modDoc = null;
            docHandler = null;
            return true;
        }

        public bool DetachEventHandlers()
        {
            DetachSwEvents();

            // Close events on all currently open documents
            DocumentEventHandler docHandler;
            int numKeys = openDocs.Count;
            object[] keys = new Object[numKeys];

            // Remove all document event handlers
            openDocs.Keys.CopyTo(keys, 0);
            foreach (ModelDoc2 key in keys)
            {
                docHandler = (DocumentEventHandler)openDocs[key];
                // Remove the pair from the hash
                docHandler.DetachEventHandlers();
                docHandler = null;
            }
            return true;
        }
        #endregion

        #region Event Handlers
        // Events
        public int ActiveDocChangeNotify()
        {
            return 0;
        }

        public int DocumentLoadNotify2(string docTitle, string docPath)
        {
            return 0;
        }

        public int FileOpenPostNotify(string FileName)
        {
            AttachEventsToAllDocuments();
            return 0;
        }

        public int FileNewNotify2(object newDoc, int docType, string templateName)
        {
            AttachEventsToAllDocuments();
            return 0;
        }

        public int ActiveModelDocChangeNotify()
        {
            return 0;
        }

        #endregion
    }

}
```
