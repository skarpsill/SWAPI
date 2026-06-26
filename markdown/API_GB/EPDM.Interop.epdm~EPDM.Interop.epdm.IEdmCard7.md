---
title: "IEdmCard7 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCard7"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard7.html"
---

# IEdmCard7 Interface

Allows you to access the file or folder data card that is created with the SOLIDWORKS PDM Professional's Card Editor.

NOTE:

Click the

Members

link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmCard7
   Inherits IEdmCard5, IEdmCard6, IEdmObject5
```

### C#

```csharp
public interface IEdmCard7 : IEdmCard5, IEdmCard6, IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmCard7 : public IEdmCard5, IEdmCard6, IEdmObject5
```

## Examples

// C# code snippet

// Taken from[IEdmCard6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard6.html)example and modified

IEdmVault5vault1 =null;IEdmFile5aFile;IEdmFolder5aFolder;IEdmCard7aCard;IEdmCardControl7aControl;intplWidth;intplHeight;intplX;intplY;intplParentCtrlID;intplPageNo;objectpoMin =null;objectpoMax =null;intvarType;intcontType;stringfileExt;intcardID;stringstr;...

publicvoidGetCardControls_Click(System.Objectsender, System.EventArgse) {try{IEdmVault7vault2 =null;if(vault1 ==null) { vault1 =newEdmVault5(); } vault2 = (IEdmVault9)vault1;if(!vault1. IsLoggedIn ) { vault1. LoginAuto (VaultsComboBox.Text,this.Handle.ToInt32()); }if((aFile !=null)) {// Get the selected file's data cardaCard = (IEdmCard7)aFolder. GetCard (fileExt); cardID = aFolder. GetCardID (fileExt); aCard. GetSize (outplWidth,outplHeight); str ="File: "+ aFile. Name +Constants.vbLf +"Card ID: "+ cardID +", EdmCardType: "+ aCard. CardType +", Width: "+ plWidth +", Height: "+ plHeight;MessageBox.Show(str);

// Get all controls in the data cardobject[]CardControlsArray = null;
aCard. GetAllControls ( out CardControlsArray);

for( int i=0; i <CardControlsArray.size(); i++)
{

object aTmpControl = CardControlsArray[i];

aControl = (IEdmCardControl7) aTmpControl;

contType = (int)aControl. ControlType ;

boolret =false;string[] variableItemsList =null;if(((contType == 7) | (contType == 8) | (contType == 9) | (contType == 10))) { str ="List values associated with drop-down card control: "+ aControl. VariableID .ToString(); ret = aControl. GetControlVariableList (aFile. ID ,outvariableItemsList);foreach(stringlistValueinvariableItemsList) { str = str +Constants.vbLf + listValue; }MessageBox.Show(str); }// Get the edit box controls on the cardif(contType == 4) { str =""; aControl. GetParentInfo (outplParentCtrlID,outplPageNo); aControl. GetPosition (outplX,outplY,outplWidth,outplHeight); varType = (int)aControl. GetValidation (outpoMin,outpoMax); str ="Card control: "+ aControl. Name ; str = str +Constants.vbLf +"Variable ID: "+ aControl. VariableID +Constants.vbLf +"EdmCardControlType: "+ contType +Constants.vbLf +"Is multi-line? "+ aControl. IsMultiLine +Constants.vbLf +"Is read-only? "+ aControl. IsReadOnly +Constants.vbLf +"Show in preview? "+ aControl. ShowInPreview ; str = str +Constants.vbLf +"Location on card: ["+ plX +", "+ plY +"], Width: "+ plWidth +", Height: "+ plHeight; str = str +Constants.vbLf +"Parent control ID (0, if none): "+ plParentCtrlID; str = str +Constants.vbLf +"Tab index: "+ plPageNo; str = str +Constants.vbLf +"EdmVariableType: "+ varType;

str = str + Constants.vbLf +"Updates all configurations? "+ aControl. UpdatesAllConfigurations .ToString();

MessageBox.Show(str); } } } }catch(System.Runtime.InteropServices.COMExceptionex) {MessageBox.Show("HRESULT = 0x"+ ex.ErrorCode.ToString("X") +" "+ ex.Message); }catch(Exceptionex) {MessageBox.Show(ex.Message); } }

## Remarks

This interface extends[IEdmCard6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard6.html)by providing the ability to get all controls in the file or folder data card.

## Accessors

[IEdmFolder5::GetCard](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetCard.html)

[IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html)with eType =[EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html).EdmObject_Card

## See Also

[IEdmCard7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard7_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
