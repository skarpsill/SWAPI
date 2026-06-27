---
title: "ModelDoc::IGetNumDependencies2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__IGetNumDependencies2.htm"
---

# ModelDoc::IGetNumDependencies2

This
method is obsolete and has been superseded by[ModelDoc2::IGetNumDependencies2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IGetNumDependencies2.htm).

Description

This method gets the number of dependencies
for the model.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = ModelDoc->IGetNumDependencies2 ( traverseFlag,
searchFlag, addReadOnlyInfo, &retval )

(Table)=========================================================

| Input: | (VARIANT_BOOL) traverseflag | TRUE if you wish to traverse down into all dependent files, FALSE if
you want only the highest level within the dependencies |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) searchflag | TRUE if you wish to apply the current search criteria, FALSE if you
want to return the dependent file information as it was stored |
| Input: | (VARIANT_BOOL) addReadOnlyInfo | TRUE if you wish to obtain read-only information with each dependent
file |
| Output: | (long*) retval | Number of strings that will be returned by ModelDoc::GetDependencies2 |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__IGetNumDependencies2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
