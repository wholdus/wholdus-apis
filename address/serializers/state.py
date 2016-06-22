def parse_state(stateQuerySet):
	states = []
	for statesItem in stateQuerySet:
		state = serialize_state(statesItem)
		states.append(state)
	return states

def serialize_state(stateItem):
	state = {}

	state["stateID"] = stateItem.id
	state["name"] = stateItem.name
	state["short_form"] = stateItem.short_form
	#state["is_union_territory"] = stateItem.is_union_territory
	#state["capital"] = stateItem.capital

	return state