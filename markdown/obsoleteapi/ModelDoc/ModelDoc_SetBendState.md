---
title: "ModelDoc::SetBendState"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc_SetBendState.htm"
---

# ModelDoc::SetBendState

This method is obsolete and has been superseded
by[ModelDoc2::SetBendState](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetBendState.htm).

Description

This method sets the current state of a sheet
metal part.

Syntax (OLE Automation)

retval = ModelDoc.SetBendState (bendState)

(Table)=========================================================

| Input: | (long) bendState | Sheet metal state to set in this part |
| --- | --- | --- |
| Return: | (long) retval | Status of the set operation |

Syntax (COM)

status = ModelDoc->SetBendState ( bendState, &retval
)

(Table)=========================================================

| Input: | (long) bendState | Sheet metal state to set in this part |
| --- | --- | --- |
| Output: | (long) retval | Status of the set operation |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The bendState value that is passed in must be one
of the values from the swSMBendState_e enumeration:

- swSMBendStateSharps the model is rolled back
  to before the first FlattenBends feature
- swSMBendStateFlattened the model is rolled
  back to just after a FlattenBends feature, but just before the corresponding
  ProcessBends feature
- swSMBendStateFolded the model is rolled back
  to just after a FlattenBends – ProcessBends feature pair.

The retval value will be one of the values from
the swSMCommandStatus_e enumeration:

- swSMErrorNone
- swSMErrorUnknown
- swSMErrorNotAPart
- swSMErrorNotASheetMetalPart
- swSMErrorInvalidBendState

If a part with bend information is edited in context
of the assembly (see AssemblyDoc::EditPart), the bend state for that part
will be set.

If this method is run on a part without bend information,
the part is not be affected and the retval is set to swSMErrorNotASheetMetalPart.
If this methodis run on an assembly, the assembly isnot be affected and
the retval is set to swSMErrorNotAPart. In both of these cases, the return
status is S_FALSE (COM only).

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc::GetBendState$$**$$ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc_SetBendState.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
