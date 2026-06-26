---
title: "Destroy Deleted Files in Vault Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Destroy_Deleted_Files_in_Vault_Example_CSharp.htm"
---

# Destroy Deleted Files in Vault Example (C#)

This example shows how to create an application that displays a form
in which
a user can select the vault in whose root
folder and subfolders all deleted files will be permanently destroyed. The user must have permission to delete
files.

**NOTE**: If using the primary interop assembly
provided with SOLIDWORKS PDM Professional, see[Using .NET Framework 4.0 in
Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

IMPORTANT:Do not recreate and run this
example if you do not want to destroy all deleted files in the root folder and
subfolders in the selected vault. Instead, SOLIDWORKS PDM Professional suggests
that you review the code to understand how you can programmatically destroy
deleted files in the root folder and subfolders of a vault.

```vb
 //--------------------------------------------------------------------------------------
 // Preconditions:
 //  1. Start Microsoft Visual Studio.
 //  2. Click File > New > Project > Visual C# > Windows Forms Application.
 //  3. Type DestroyDeletedItemsCSharp in Name.
 //  4. Click the Browse button and browse to the folder where to create
 //     the project.
 //  5. Click OK.
 //  6. Replace the code in Form1.cs with this code.
 //  7. Replace the code in Form1.Designer.cs with this code.
 //  8. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 //     name in the Solution Explorer, click Add Reference, click Framework
 //     in the left-side panel, browse to the top folder of your SOLIDWORKS
 //     PDM Professional installation, locate and click  EPDM.Interop.epdm.dll,
 //     click Open, click Add, and click  Close).
 //  9. Right-click EPDM.Interop.epdm in References, click Properties, and
 //     set Embed Interop Types to False to handle methods that pass arrays
 //     of structures.
 // 10. Switch back to the Form1.cs code window.
 // 11. Ensure that the namespaces specified in all of the *.cs files match
 //     the project name.
// 12. Delete one or more checked-in files from the root folder of your vault.
 // 13. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 //  1. Displays the Destroy Deleted Files dialog.
 //  2. Select a vault.
 //  3. Optionally select the Include all subfolders check box.
 //  4. Click the Destroy deleted files button.
 //     A message box pops up informing you that:
 //     * No deleted files were found to destroy.
 //       - or -
 //     * The deleted files were destroyed.
 //  5. Click OK in the message box.
 //  6. Close the Destroy Deleted Files dialog.
 //--------------------------------------------------------------------------------------

 //
```

Form1.cs

```vb
using System;
 using System.Windows.Forms;
 using EPDM.Interop.epdm;

 namespace DestroyDeletedItems
 {
```

publicpartialclassForm1: Form

{

voidDestroyDeletedItems_Load(objectsender, EventArgs e)

{

try

{

//Declare and create an instance of IEdmVault5

IEdmVault5 vault1 =newEdmVault5();

//Cast IEdmVault5 to IEdmVault8

IEdmVault8 vault = (IEdmVault8)vault1;

EdmViewInfo[] Views =null;

//Populate the form with the names of

//the vaults on the computer

vault. GetVaultViews (outViews,false);

VaultsComboBox.Items.Clear();

foreach(EdmViewInfo ViewinViews)

{

VaultsComboBox.Items.Add(View.mbsVaultName);

}

if(VaultsComboBox.Items.Count > 0)

{

VaultsComboBox.Text = (string)VaultsComboBox.Items[0];

}

}

catch(System.Runtime.InteropServices.COMException ex)

{

MessageBox.Show("HRESULT = 0x"+ ex.ErrorCode.ToString("X") + ex.Message);

}

catch(Exception ex)

{

MessageBox.Show(ex.Message);

}

}

voidDestroyDeletedItemsButton_Click(objectsender, EventArgs e)

{

try

{

//Declare and create an instance of IEdmVault5

IEdmVault5 vault =newEdmVault5();

//Log into selected vault as the current user

vault. LoginAuto (VaultsComboBox.Text,this.Handle.ToInt32());

//Check to see if deleted files should be

//destroyed in all the subfolders

boolaRecursive =false;

if(CheckBox_Recursive.Checked)

{

aRecursive =true;

}

EdmDeletedItems[] poDeletedItems =null;

EdmFileInfo[] ppoDestroyedItems =null;

EdmBatchDelErrInfo[] poErrors =null;

IEdmFolder5 DeletedFolder1 =default(IEdmFolder5);

//Get the root folder of the vault

DeletedFolder1 = vault. RootFolder ;

IEdmFolder13 DeletedFolder = (IEdmFolder13)DeletedFolder1;

DeletedFolder. GetDeletedItems (outpoDeletedItems,true);

//Destroy all deleted files in the root folder and

//subfolders, if the check box is selected on the form

DeletedFolder. DestroyDeletedItems2 (poDeletedItems,outppoDestroyedItems,outpoErrors);

//If any deleted files found, display their names in a message box

stringmsg =null;

intidx = 0;

foreach(EdmFileInfo ppoDestroyedIteminppoDestroyedItems)

{

stringrow =null;

row ="\nDocumentID: "+ Convert.ToString(ppoDestroyedItem. mlFileID ) +", FolderID: "+ Convert.ToString(ppoDestroyedItem. mlFolderID ) +", File path: "+ ppoDestroyedItem. mbsPath ;

if(ppoDestroyedItem. mhResult == 0)

{

row = row +"\nStatus: OK\n";

}

else

{

EdmBatchDelErrInfo[] poError =null;

row = row +" status: Failed="+"HRESULT = 0x"+ Convert.ToString(poError[idx]. mlErrorCode );

idx += 1;

}

msg = msg + row;

}

if(msg ==null)

{

MessageBox.Show("No deleted files were found in the selected
vault's root folder or \n subfolders.");

}

else

{

MessageBox.Show("The status for each destroyed file is:\n"+ msg);

}

}

catch(System.Runtime.InteropServices.COMException ex)

{

MessageBox.Show("HRESULT = 0x"+ ex.ErrorCode.ToString("X")
+ ex.Message);

}

catch(Exception ex)

{

MessageBox.Show(ex.Message);

}

}

voidCheckBox_Recursive_CheckedChanged(objectsender, EventArgs e)

{

}

privatevoidlabel1_Click(objectsender, EventArgs e)

{

}

}

```vb
 }
Back to top
 //Form1.Designer.cs
namespace DestroyDeletedItems
 {
```

partialclassForm1

{

///<summary>

///Required designer variable.

///</summary>

privateSystem.ComponentModel.IContainer components =null;

///<summary>

///Clean up any resources being used.

///</summary>

///<param name="disposing">true
if managed resources should be disposed; otherwise, false.</param>

protectedoverridevoidDispose(booldisposing)

{

if(disposing && (components !=null))

{

components.Dispose();

}

base.Dispose(disposing);

}

#regionWindows Form Designer
generated code

///<summary>

///Required method for Designer support - do not modify

///the contents of this method with the code editor.

///</summary>

privatevoidInitializeComponent()

{

this.components =newSystem.ComponentModel.Container();

this.AutoScaleMode =
System.Windows.Forms.AutoScaleMode.Font;

this.ClientSize =newSystem.Drawing.Size(800, 450);

this.Text ="Form1";

this.label1 =newSystem.Windows.Forms.Label();

this.VaultsLabel =newSystem.Windows.Forms.Label();

this.VaultsComboBox =newSystem.Windows.Forms.ComboBox();

this.DestroyDeletedItemsButton =newSystem.Windows.Forms.Button();

this.CheckBox_Recursive =newSystem.Windows.Forms.CheckBox();

this.SuspendLayout();

//

// label1

//

this.label1.Location
=newSystem.Drawing.Point(32, 19);

this.label1.Name ="label1";

this.label1.Size =newSystem.Drawing.Size(187, 79);

this.label1.TabIndex = 0;

this.label1.Text ="This application destroys all deleted files in the root folder of the selected va"+

"ult and also allows you to destroy all deleted files in all of the selected vaul"+

"t\'s subfolders.";

this.label1.Click +=newSystem.EventHandler(this.label1_Click);

//

// VaultsLabel

//

this.VaultsLabel.AutoSize
=true;

this.VaultsLabel.Location =newSystem.Drawing.Point(35, 113);

this.VaultsLabel.Name ="VaultsLabel";

this.VaultsLabel.Size =newSystem.Drawing.Size(75, 13);

this.VaultsLabel.TabIndex = 1;

this.VaultsLabel.Text ="Select a vault:";

//

// VaultsComboBox

//

this.VaultsComboBox.FormattingEnabled
=true;

this.VaultsComboBox.Location =newSystem.Drawing.Point(35, 130);

this.VaultsComboBox.Name ="VaultsComboBox";

this.VaultsComboBox.Size =newSystem.Drawing.Size(184, 21);

this.VaultsComboBox.TabIndex = 2;

//

// DestroyDeletedItemsButton

//

this.DestroyDeletedItemsButton.Location
=newSystem.Drawing.Point(35, 229);

this.DestroyDeletedItemsButton.Name
="DestroyDeletedItemsButton";

this.DestroyDeletedItemsButton.Size
=newSystem.Drawing.Size(184, 23);

this.DestroyDeletedItemsButton.TabIndex
= 4;

this.DestroyDeletedItemsButton.Text
="Destroy deleted files";

this.DestroyDeletedItemsButton.UseVisualStyleBackColor
=true;

this.DestroyDeletedItemsButton.Click
+=newSystem.EventHandler(this.DestroyDeletedItemsButton_Click);

//

// CheckBox_Recursive

//

this.CheckBox_Recursive.AutoSize
=true;

this.CheckBox_Recursive.Location =newSystem.Drawing.Point(38, 174);

this.CheckBox_Recursive.Name ="CheckBox_Recursive";

this.CheckBox_Recursive.Size =newSystem.Drawing.Size(125, 17);

this.CheckBox_Recursive.TabIndex =
5;

this.CheckBox_Recursive.Text ="Include all subfolders";

this.CheckBox_Recursive.UseVisualStyleBackColor
=true;

this.CheckBox_Recursive.CheckedChanged
+=newSystem.EventHandler(this.CheckBox_Recursive_CheckedChanged);

//

// Form1

//

this.AutoScaleDimensions
=newSystem.Drawing.SizeF(6F, 13F);

this.AutoScaleMode =
System.Windows.Forms.AutoScaleMode.Font;

this.ClientSize =newSystem.Drawing.Size(254, 274);

this.Controls.Add(this.CheckBox_Recursive);

this.Controls.Add(this.DestroyDeletedItemsButton);

this.Controls.Add(this.VaultsComboBox);

this.Controls.Add(this.VaultsLabel);

this.Controls.Add(this.label1);

this.Name ="Form1";

this.Text ="Destroy Deleted Files";

this.Load +=newSystem.EventHandler(this.DestroyDeletedItems_Load);

this.ResumeLayout(false);

this.PerformLayout();

}

#endregion

privateSystem.Windows.Forms.Label label1;

privateSystem.Windows.Forms.Label VaultsLabel;

privateSystem.Windows.Forms.ComboBox VaultsComboBox;

privateSystem.Windows.Forms.Button DestroyDeletedItemsButton;

privateSystem.Windows.Forms.CheckBox CheckBox_Recursive;

}

```vb
 }
```

```vb
 Back to top
```
