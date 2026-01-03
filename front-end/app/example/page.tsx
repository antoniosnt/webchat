import React, { FC } from "react";

interface DefaultProps {
  foo: string;
}

const TestComponent: FC<DefaultProps> = ({ foo = "Test Component" }) => {
  return <div>{foo}</div>;
};

export default TestComponent;
