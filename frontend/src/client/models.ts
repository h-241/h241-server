


export type HTTPValidationError = {
	detail?: Array<ValidationError>;
};



export type Message = {
	message: string;
};






export type ValidationError = {
	loc: Array<string | number>;
	msg: string;
	type: string;
};

