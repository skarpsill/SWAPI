---
title: "FeatureManager::InsertMacroFeature2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertMacroFeature2.htm"
---

# FeatureManager::InsertMacroFeature2

This method is obsolete and has been superseded
by[FeatureManager::InsertMacroFeature3](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertMacroFeature3.htm).

Description

This method inserts a macro
feature in this model.

Syntax (OLE Automation)

retval = FeatureManager.InsertMacroFeature2 ( baseName,
progId, macroMethods, paramNames, paramTypes, paramValues, dimTypes, dimValues,
editBody, iconFiles, options)

(Table)=========================================================

| Input: | (BSTR) baseName | Name of the base feature (see Remarks ) |
| --- | --- | --- |
| Input: | (BSTR) progId | Indicates whether to use COM
or VBA callback methods (see Remarks ) |
| Input: | (VARIANT) macroMethods | Array of size 9 in string (see Remarks ) |
| Input: | (VARIANT) paramNames | Array of parameters |
| Input: | (VARIANT) paramTypes | Array of types of parameters
of size paramCount as defined by swMacroFeatureParamType_e |
| Input: | (VARIANT) paramValues | Array of values of parameters |
| Input: | (VARIANT) dimTypes | Array of types of dimensions
as defined in swDimensionType_e (see Remarks ) |
| Input: | (VARIANT) dimValues | Array of values of the dimensions |
| Input: | (LPBODY2) editBody | Body to modify in the macro feature |
| Input: | (VARIANT) iconFiles | Array of 3 strings (.bmp files)
(see Remarks) |
| Input: | (long) options | Placement of the macro feature
in the FeatureManager design tree as defined by swMacroFeatureOptions_e |
| Output: | (LPFEATURE*) retval | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->IInsertMacroFeature2
( baseName, progId, *macroMethods, paramCount, *paramNames, *paramTypes,
*paramValues, dimCount, *dimTypes, *dimCountValues, editBody, iconCount,
*iconFiles, options, &retval)

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) baseName | Name of the base feature (see Remarks ) |
| --- | --- | --- |
| Input: | (BSTR) progId | Indicates whether to use COM or VBA callback
methods (see Remarks ) |
| Input: | (BSTR *) *macroMethods | Array of size 9 in string (see Remarks ) |
| Input: | (long) paramCount | Number of parameters |
| Input: | (BSTR *) *paramNames | Array of parameters of size paramCount |
| Input: | (long *) *paramTypes | Array of types of parameters
of size paramCount as defined by swMacroFeatureParamType_e |
| Input: | (BSTR *) *paramValues | Array of values of parameters
of size paramCount |
| Input: | (long) dimCount | Number of dimensions |
| Input: | (long *) *dimTypes | Array of types of dimensions as defined by swDimensionType_e
(see Remarks ) |
| Input: | (double *) *dimCountValues | Array of doubles of values of
dimensions of size dimCount |
| Input: | (LPBODY2) editBody | Body to modify in the macro feature |
| Input: | (long) iconCount | Number of icons |
| Input: | (BSTR *) *iconFiles | Array of 3 strings (see Remarks ) |
| Input: | (long) options | Placement of the macro feature
in the FeatureManager design tree as defined by swMacroFeatureOptions_e |
| Input: | (LPFEATURE*) retval | Pointer to the Feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

baseName

- The
  argument baseName is serialized within the feature and cannot be changed.
- You
  can find out the name of the base feature by using MacroFeatureData::GetBaseName.
- The baseName argument is also used to generate
  the name of the feature when the feature is first created.

ProgId

(Table)=========================================================

| To create a macro feature using the OLE version
from VB or VBA... | Then the input arguments should be... |
| --- | --- |
| COM callback methods | The progId argument is the name of the program ID for the component
that implements the COM callback methods. The object that is represented
by progID must support the swComFeature interface. InsertMacroFeature2 ("Sample", "Sample.MyFeature",
_ Nothing,
paramNames, paramTypes, _ paramValues,
dimTypes, dimValues, _ editbody,
iconFiles, _ swMacroFeatureByDefault) In the COM server, the Sample.Feature class is derived or supports the
SwComFeature interface methods. These methods support the macro feature's
rebuild, edit, and security functions. |
| VBA callback methods | InsertMacroFeature ( "", callBackMethods ... ) |

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

macroMethods

The macroMethods argument is implemented
from VBA only and is a nine (9) element array of strings consisting of
the following values:

Filename should be the full pathname to the
macro file. If the procedures are all self-contained in the same macro
file that calls FeatureManager::InsertMacroFeature2, then a call to SldWorks::GetCurrentMacroPathName
will provide all of the information necessary for the Filename.

If a security procedure is not used, then
Filename, Module, and Procedure must all be empty strings.

Procedure namesmusthave answmprefix in the name.
This prefix identifies the procedures to execute.

dimTypes

Only these dimension types are supported
by this method:

- swAngularDimension
- swLinearDimension
- swRadialDimension

iconFiles

VARIANT containing an array of three strings
that refer to Windows bitmap images for the regular, suppressed, and highlighted
images for the custom macro feature icon.

- Images must be Windows
  bitmap (*.bmp) format and be 16 pixels wide X 18 pixels high
- Either the full pathname
  or only the filename can be used; for example,c:\bitmaps\icon1.bmporicon1.bmp.
- The first string in
  the array is for the regular icon bitmap, the second string is for suppressed
  icon bitmap, and the third string is for highlighted icon bitmap.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\FeatureManager\FeatureManager__InsertMacroFeature2.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="FeatureManager_Object$$**$$Body2_Object$$**$$FeatureData_Object$$**$$MacroFeatureData_Object$$**$$IntroMacro$$**$$MacroFeatureDataIcons$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\FeatureManager\FeatureManager__InsertMacroFeature2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="EXCutBodyInHalfUsingMacroFeature$$**$$MacroFeatureDimensions$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\FeatureManager\FeatureManager__InsertMacroFeature2.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
